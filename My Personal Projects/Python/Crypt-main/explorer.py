import os
import argparse
import zstandard as zstd
from tqdm import tqdm

def read_line(stream):
    """
    Reads bytes from the stream until a newline character is found.
    Returns the bytes read without the newline character.
    """
    line = b''
    while True:
        c = stream.read(1)
        if not c:
            if line:
                return line
            else:
                return None
        if c == b'\n':
            break
        line += c
    return line

def is_safe_path(base_path, target_path):
    """
    Ensures that the target path is within the base path to prevent path traversal attacks.
    """
    abs_base = os.path.abspath(base_path)
    abs_target = os.path.abspath(target_path)
    return abs_target.startswith(abs_base)

def extract_archive(input_file, output_dir, verbose=False):
    """
    Extracts the archive created by the backup script.
    """
    # First, we need to determine the total number of files to extract
    total_files = 0

    # Open the compressed file to count the files
    with open(input_file, 'rb') as compressed_file:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(compressed_file) as decomp_stream:
            while True:
                # Read the relative path
                rel_path_bytes = read_line(decomp_stream)
                if rel_path_bytes is None:
                    break  # End of file
                rel_path_str = rel_path_bytes.decode('utf-8').strip()
                if not rel_path_str:
                    continue
                # Read the total size
                total_size_bytes = read_line(decomp_stream)
                if total_size_bytes is None:
                    break
                total_size_str = total_size_bytes.decode('utf-8').strip()
                if not total_size_str:
                    break
                try:
                    total_size = int(total_size_str)
                except ValueError:
                    break
                # Skip over the file content
                bytes_remaining = total_size
                while bytes_remaining > 0:
                    chunk_size = min(8192, bytes_remaining)
                    chunk = decomp_stream.read(chunk_size)
                    if not chunk:
                        break
                    bytes_remaining -= len(chunk)
                # Read the newline after file content
                decomp_stream.read(1)
                total_files += 1

    # Now, perform the actual extraction
    with open(input_file, 'rb') as compressed_file:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(compressed_file) as decomp_stream:
            pbar = tqdm(total=total_files, desc="Extracting", unit="file", disable=verbose)
            while True:
                # Read the relative path
                rel_path_bytes = read_line(decomp_stream)
                if rel_path_bytes is None:
                    break  # End of file
                rel_path_str = rel_path_bytes.decode('utf-8').strip()
                if not rel_path_str:
                    continue
                rel_path = rel_path_str

                # Read the total size
                total_size_bytes = read_line(decomp_stream)
                if total_size_bytes is None:
                    print("Unexpected end of file when reading file size.")
                    break
                total_size_str = total_size_bytes.decode('utf-8').strip()
                if not total_size_str:
                    print(f"Unexpected empty file size for {rel_path}.")
                    break
                try:
                    total_size = int(total_size_str)
                except ValueError:
                    print(f"Invalid file size for {rel_path}.")
                    break

                # Ensure the output path is safe
                output_path = os.path.join(output_dir, rel_path)
                if not is_safe_path(output_dir, output_path):
                    print(f"Warning: Skipping potentially unsafe path: {rel_path}")
                    # Skip reading the file content
                    bytes_remaining = total_size
                    while bytes_remaining > 0:
                        chunk_size = min(8192, bytes_remaining)
                        chunk = decomp_stream.read(chunk_size)
                        if not chunk:
                            break
                        bytes_remaining -= len(chunk)
                    # Read and discard the newline after file content
                    decomp_stream.read(1)
                    continue

                # Create directories if they don't exist
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Read the file content and write it to the output file
                bytes_remaining = total_size
                bytes_read = 0
                try:
                    with open(output_path, 'wb') as out_file:
                        while bytes_remaining > 0:
                            chunk_size = min(8192, bytes_remaining)
                            chunk = decomp_stream.read(chunk_size)
                            if not chunk:
                                print(f"Unexpected end of file when reading content of {rel_path}.")
                                break
                            out_file.write(chunk)
                            bytes_read += len(chunk)
                            bytes_remaining -= len(chunk)
                    if verbose:
                        print(f"Extracted: {rel_path}")
                except Exception as e:
                    print(f"Failed to write {rel_path}: {e}")
                    # Skip reading the remaining bytes and the newline
                    while bytes_remaining > 0:
                        decomp_stream.read(min(8192, bytes_remaining))
                        bytes_remaining -= min(8192, bytes_remaining)
                    decomp_stream.read(1)  # Read the newline
                    continue

                # Verify if bytes read matches total_size
                if bytes_read != total_size:
                    print(f"Warning: Mismatch in file size for {rel_path}. Expected {total_size} bytes, got {bytes_read} bytes.")
                    # Attempt to realign by reading until the next newline
                    while True:
                        c = decomp_stream.read(1)
                        if not c or c == b'\n':
                            break
                else:
                    # Read the newline after file content
                    newline = decomp_stream.read(1)
                    if newline != b'\n':
                        print(f"Expected newline after file content of {rel_path}, but got something else.")
                        # Attempt to realign the stream
                        while True:
                            c = decomp_stream.read(1)
                            if not c or c == b'\n':
                                break

                if not verbose:
                    pbar.update(1)

            if not verbose:
                pbar.close()

    print("Extraction completed successfully!")

def main():
    parser = argparse.ArgumentParser(description="Extract archives created by the backup script.")
    parser.add_argument("input_file", type=str, help="Path to the .zst archive file to extract.")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory to extract files to.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output to show file operations.")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Input file not found: {args.input_file}")
        return

    # Determine the default output directory based on the input file name
    if args.output_dir is None:
        base_name = os.path.basename(args.input_file)
        if base_name.endswith('.zst'):
            base_name = base_name[:-4]
        args.output_dir = os.path.join('.', base_name)

    os.makedirs(args.output_dir, exist_ok=True)

    extract_archive(args.input_file, args.output_dir, args.verbose)

if __name__ == "__main__":
    main()
