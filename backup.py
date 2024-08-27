import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if the source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if the destination directory exists, if not create it
    if not os.path.isdir(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist. Creating it.")
        os.makedirs(dest_dir)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        
        # Skip directories
        if os.path.isdir(source_file):
            continue

        dest_file = os.path.join(dest_dir, filename)
        
        # Check if file already exists in the destination directory
        if os.path.exists(dest_file):
            # Append timestamp to the filename
            base, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_filename = f"{base}_{timestamp}{ext}"
            dest_file = os.path.join(dest_dir, new_filename)

        # Copy the file
        try:
            shutil.copy2(source_file, dest_file)
            print(f"Copied: {source_file} -> {dest_file}")
        except Exception as e:
            print(f"Error copying file '{source_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <dest_dir>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)
