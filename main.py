import os
import shutil
import sys


def find_all_files(source, extension):
    """Search for all files with the specified extension in the source directory."""
    files = []
    for root, dirs, files_in_dir in os.walk(source):
        for file in files_in_dir:
            if file.endswith(extension):
                files.append(os.path.join(root, file))
    return files


def create_dir(path):
    """Create the target directory if it doesn't exist."""
    if not os.path.exists(path):
        os.mkdir(path)


def copy_files(source_files, target):
    """Copy all found files to the target directory."""
    create_dir(target)
    for file in source_files:
        shutil.copy(file, target)


def main(source, target, extension):
    """Main function to search and copy files."""
    # Find files in the source directory
    source_files = find_all_files(source, extension)

    # Copy the found files to the target directory
    copy_files(source_files, target)

    print(f"Found and copied {len(source_files)} '{extension}' files from '{source}' to '{target}'.")


if __name__ == "__main__":
    # Ensure the script is called with the correct arguments
    args = sys.argv
    if len(args) != 4:
        raise Exception("You must pass a source directory, target directory, and file extension.")

    source_dir, target_dir, file_extension = args[1:]

    # Call the main function
    main(source_dir, target_dir, file_extension)
