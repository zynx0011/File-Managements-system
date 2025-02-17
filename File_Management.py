import os
import shutil


def handle_path(directory, filename=None):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return None

    if filename:
        path = os.path.join(directory, filename)
        if not os.path.exists(path):
            print(f"Error: '{filename}' does not exist in '{directory}'.")
            return None
        return path

    return directory


def list_files(directory):
    dir_path = handle_path(directory)
    if not dir_path:
        return
    print(f"\nDirectory contents of '{directory}':")
    files = os.listdir(directory)
    print("The directory is empty." if not files else "\n".join(files))


def rename(directory, oldname, newname):
    old_path = handle_path(directory, oldname)
    if not old_path:
        return

    new_path = os.path.join(directory, newname)
    try:
        os.rename(old_path, new_path)
        print(f"Renamed '{oldname}' to '{newname}'.")
    except PermissionError:
        print(f"Error: Permission denied to rename '{oldname}'.")


def delete(directory, filename):
    path = handle_path(directory, filename)
    if not path:
        return

    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Deleted directory '{filename}'.")
        else:
            os.remove(path)
            print(f"Deleted file '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to delete '{filename}'.")


def copy(directory, filename, target_directory):
    source_path = handle_path(directory, filename)
    target_dir = handle_path(target_directory)

    if not source_path or not target_dir:
        return

    target_path = os.path.join(target_directory, filename)
    try:
        shutil.copy(source_path, target_path)
        print(f"Copied '{filename}' to '{target_directory}'.")
    except PermissionError:
        print(f"Error: Permission denied to copy '{filename}'.")


def create(directory, filename):
    dir_path = handle_path(directory)
    if not dir_path:
        return

    path = os.path.join(directory, filename)
    if os.path.exists(path):
        print(f"Error: '{filename}' already exists in '{directory}'.")
        return

    try:
        with open(path, "w") as file:
            pass
        print(f"Created file '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to create '{filename}'.")


def main():
    while True:
        print("\nFile Management System")
        print("1. Create a file")
        print("2. Delete a file or directory")
        print("3. Copy a file")
        print("4. Rename a file or directory")
        print("5. List files in a directory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            directory = input("Enter directory path: ")
            filename = input("Enter file name: ")
            create(directory, filename)

        elif choice == "2":
            directory = input("Enter directory path: ")
            filename = input("Enter file or directory name: ")
            delete(directory, filename)

        elif choice == "3":
            directory = input("Enter source directory path: ")
            filename = input("Enter file name: ")
            target_directory = input("Enter target directory path: ")
            copy(directory, filename, target_directory)

        elif choice == "4":
            directory = input("Enter directory path: ")
            oldname = input("Enter current file name: ")
            newname = input("Enter new file name: ")
            rename(directory, oldname, newname)

        elif choice == "5":
            directory = input("Enter directory path: ")
            list_files(directory)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



main()
