# Backup and Extraction Tools

## Overview

This project contains two command-line programs for compressing directories into `.zst` archive files and extracting these files. The tools are designed for backup and restoration of various system and user directories.

### Programs Included:
1. **Archivist**: Compresses directories into a `.zst` archive for efficient storage.
2. **Explorer**: Extracts files from a `.zst` archive created by the backup script.

## Installation

To use these scripts, make sure the following dependencies are installed:

- Python 3
- [Zstandard](https://pypi.org/project/zstandard/):
  ```sh
  pip install zstandard
  ```
- [TQDM](https://pypi.org/project/tqdm/):
  ```sh
  pip install tqdm
  ```
- [Colorama](https://pypi.org/project/colorama/):
  ```sh
  pip install colorama
  ```
- [Aiofiles](https://pypi.org/project/aiofiles/):
  ```sh
  pip install aiofiles
  ```

## Backup Script

### Usage

Archivist allows you to compress predefined user or system directories into a `.zst` file for easy backup.

```sh
python archivist.py [OPTIONS]
```

### Available Options

- `--documents`           : Backup the Documents folder
- `--desktop`             : Backup the Desktop folder
- `--downloads`           : Backup the Downloads folder
- `--pictures`            : Backup the Pictures folder
- `--videos`              : Backup the Videos folder
- `--appdata`             : Backup the AppData folder
- `--program-files`       : Backup the Program Files folder
- `--program-files-x86`   : Backup the Program Files (x86) folder
- `--path <FOLDER_PATH>`  : Backup a specific folder by providing its path
- `--ignore-file <FILE>`  : Path to a text file containing directories to ignore
- `--verbose`             : Enable verbose output to show file operations

### Example

To backup the Documents and Downloads folders:
```sh
python archivist.py --documents --downloads
```

To backup a specific folder by providing its path:
```sh
python archivist.py --path "C:\MyFolder"
```

## Extraction Script

### Usage

Explorer allows you to decompress the `.zst` archive and restore the backed-up files.

```sh
python explorer.py <INPUT_FILE> [OPTIONS]
```

### Available Options

- `<INPUT_FILE>`           : Path to the `.zst` archive file to extract
- `--output-dir <FOLDER>`  : Directory to extract files to (default is a folder named after the archive)
- `--verbose`              : Enable verbose output to show file operations

### Example

To extract an archive named `Documents.zst`:
```sh
python explorer.py Documents.zst
```

To extract into a specific folder:
```sh
python explorer.py Documents.zst --output-dir "C:\RestoredFiles"
```
