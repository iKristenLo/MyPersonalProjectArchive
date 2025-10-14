import os
import argparse
import zstandard as zstd
import asyncio
import aiofiles
import colorama
from colorama import Fore, Style
import sys

# Initialize colorama
colorama.init(autoreset=True)

def get_directory_path(directory_name):
    """
    Gets the path for a given directory.
    For user directories, it looks in the user's home or OneDrive directories.
    For system directories like 'Program Files', it looks in the system root.
    """
    # Directories located in the user's home directory
    user_directories = ['Documents', 'Desktop', 'Downloads', 'Pictures', 'Videos', 'AppData']

    # Directories located in the system drive root
    system_directories = ['Program Files', 'Program Files (x86)']

    if directory_name in user_directories:
        user_home = os.path.expanduser('~')
        standard_path = os.path.join(user_home, directory_name)
        onedrive_path = os.path.join(user_home, 'OneDrive', directory_name)
        
        if os.path.exists(standard_path):
            return standard_path
        elif os.path.exists(onedrive_path):
            print(f"{Fore.YELLOW}Using OneDrive path for {directory_name}{Style.RESET_ALL}")
            return onedrive_path
        else:
            return None
    elif directory_name in system_directories:
        # For system directories, ensure system_drive ends with a backslash
        system_drive = os.environ.get('SystemDrive', 'C:')
        if not system_drive.endswith(os.sep):
            system_drive += os.sep
        standard_path = os.path.join(system_drive, directory_name)
        if os.path.exists(standard_path):
            return standard_path
        else:
            return None
    else:
        # If directory_name is not recognized, return None
        return None

def should_skip_file(file_path):
    """
    Determines whether a file should be skipped during compression.
    """
    # Define files or patterns to skip
    skip_files = ['parent.lock', 'lock', '.DS_Store', 'Thumbs.db']
    if os.path.basename(file_path) in skip_files:
        return True
    return False

def count_files(directory, ignore_dirs):
    """
    Counts the number of files to be processed, excluding ignored files.
    """
    total_files = 0
    for dirpath, _, filenames in os.walk(directory):
        if any(os.path.abspath(ignored) in os.path.abspath(dirpath) for ignored in ignore_dirs):
            continue
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if should_skip_file(file_path):
                continue
            total_files += 1
    return total_files

async def compress_file(file_info, zstd_writer, progress_dict, lock, verbose=False):
    """
    Compresses a single file.
    """
    file_path, rel_path = file_info

    try:
        # Initialize progress
        async with lock:
            progress_dict[rel_path] = 0

        # First pass to get total_size
        total_size = 0
        async with aiofiles.open(file_path, "rb") as f:
            while True:
                chunk = await f.read(8192)
                if not chunk:
                    break
                total_size += len(chunk)
        
        # Write file metadata
        file_metadata = f"{rel_path}\n{total_size}\n".encode()
        zstd_writer.write(file_metadata)

        # Read and write content in chunks
        copied_size = 0
        async with aiofiles.open(file_path, "rb") as f:
            while True:
                chunk = await f.read(8192)
                if not chunk:
                    break
                zstd_writer.write(chunk)
                copied_size += len(chunk)
                progress = (copied_size / total_size) * 100
                async with lock:
                    progress_dict[rel_path] = progress

        # Write newline after file content
        zstd_writer.write(b"\n")

        async with lock:
            progress_dict[rel_path] = 100

    except Exception as e:
        error_msg = str(e)
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {file_path} - {error_msg}")
        async with lock:
            progress_dict[rel_path] = -1

async def display_progress(progress_dict, total_files, lock):
    """
    Displays the compression progress.
    """
    while True:
        async with lock:
            # Clear the console
            sys.stdout.write("\033[2J\033[H")
            # Calculate overall progress
            total_completed = len([f for f in progress_dict if progress_dict[f] >= 100 or progress_dict[f] == -1])
            overall_progress = total_completed / total_files * 100
            print(f"{Fore.CYAN}Overall Progress: {overall_progress:.2f}% ({total_completed}/{total_files}){Style.RESET_ALL}\n")

            # Display progress for each file still in progress
            in_progress_files = False
            for rel_path, progress in progress_dict.items():
                if progress >= 100 or progress == -1:
                    continue  # Don't display completed or errored files
                else:
                    in_progress_files = True
                    status = f"{Fore.YELLOW}[{progress:.1f}%]{Style.RESET_ALL}"
                    print(f"{status} {rel_path}")
            if not in_progress_files and total_completed < total_files:
                print(f"{Fore.GREEN}Waiting for files to start processing...{Style.RESET_ALL}")
        sys.stdout.flush()
        await asyncio.sleep(0.5)
        if total_completed == total_files:
            break

async def compress_directory(source_dir, output_dir, total_files, ignore_dirs, verbose=False):
    base_name = os.path.basename(os.path.normpath(source_dir))
    output_file = os.path.join(output_dir, f"{base_name}.zst")
    
    progress_dict = {}  # Dictionary to track progress of each file
    lock = asyncio.Lock()  # Lock to synchronize access to progress_dict

    with open(output_file, "wb") as f:
        cctx = zstd.ZstdCompressor()
        with cctx.stream_writer(f) as zstd_writer:
            # Build a list of files to process
            file_list = []
            for dirpath, _, filenames in os.walk(source_dir):
                if any(os.path.abspath(ignored) in os.path.abspath(dirpath) for ignored in ignore_dirs):
                    continue
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    if should_skip_file(file_path):
                        continue
                    rel_path = os.path.relpath(file_path, source_dir)
                    file_list.append((file_path, rel_path))
            
            # Start a task to display progress
            progress_task = asyncio.create_task(display_progress(progress_dict, total_files, lock))
            
            # Process files sequentially to ensure data integrity
            for file_info in file_list:
                await compress_file(file_info, zstd_writer, progress_dict, lock, verbose)
            
            # Wait for progress display to finish
            await progress_task

def backup_directory(directory, output_dir, ignore_dirs, verbose=False, is_custom_path=False):
    if is_custom_path:
        dir_path = os.path.abspath(directory)
        if not os.path.exists(dir_path):
            print(f"{Fore.RED}Directory not found: {directory}{Style.RESET_ALL}")
            return
    else:
        dir_path = get_directory_path(directory)
        if not dir_path:
            print(f"{Fore.RED}Directory not found: {directory}{Style.RESET_ALL}")
            return

    total_files = count_files(dir_path, ignore_dirs)
    if total_files == 0:
        print(f"{Fore.YELLOW}No files to backup in {directory}.{Style.RESET_ALL}")
        return
    asyncio.run(compress_directory(dir_path, output_dir, total_files, ignore_dirs, verbose))

def main():
    parser = argparse.ArgumentParser(description="Backup filesystem with compression")
    parser.add_argument("--documents", action="store_true", help="Backup Documents folder")
    parser.add_argument("--desktop", action="store_true", help="Backup Desktop folder")
    parser.add_argument("--downloads", action="store_true", help="Backup Downloads folder")
    parser.add_argument("--pictures", action="store_true", help="Backup Pictures folder")
    parser.add_argument("--videos", action="store_true", help="Backup Videos folder")
    parser.add_argument("--appdata", action="store_true", help="Backup AppData folder")
    parser.add_argument("--program-files", action="store_true", help="Backup Program Files folder")
    parser.add_argument("--program-files-x86", action="store_true", help="Backup Program Files (x86) folder")
    parser.add_argument("--path", type=str, help="Backup a specific folder by providing its path")
    parser.add_argument("--ignore-file", type=str, help="Path to a text file containing directories to ignore")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output to show file operations")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "backup_output")
    os.makedirs(output_dir, exist_ok=True)

    # Load ignore directories from file
    ignore_dirs = []
    if args.ignore_file:
        try:
            with open(args.ignore_file, 'r') as f:
                ignore_dirs = [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"{Fore.RED}[ERROR] Ignore file not found: {args.ignore_file}{Style.RESET_ALL}")
            return

    directories = {
        "Documents": "Documents",
        "Desktop": "Desktop",
        "Downloads": "Downloads",
        "Pictures": "Pictures",
        "Videos": "Videos",
        "AppData": "AppData",
        "Program Files": "Program Files",
        "Program Files (x86)": "Program Files (x86)"
    }

    selected_dirs = [
        name for name in directories.keys()
        if getattr(args, name.lower().replace(" ", "_").replace("(", "").replace(")", ""))
    ]

    # Backup predefined directories
    for directory in selected_dirs:
        backup_directory(directories[directory], output_dir, ignore_dirs, args.verbose)

    # Backup custom path if provided
    if args.path:
        backup_directory(args.path, output_dir, ignore_dirs, args.verbose, is_custom_path=True)

    print(f"{Fore.GREEN}Backup completed successfully!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
