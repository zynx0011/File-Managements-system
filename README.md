

---

# File Management System

A simple Python-based **File Management System** that allows users to perform basic file operations such as creating, renaming, deleting, copying, and listing files within a specified directory. This program handles **PermissionError** to ensure the system doesn't crash when users lack permissions to perform certain actions.

## Features

- **Create a file**: Create an empty file in a specified directory.
- **Delete a file or directory**: Remove a file or an entire directory.
- **Copy a file**: Copy a file from one directory to another.
- **Rename a file or directory**: Rename an existing file or directory.
- **List files in a directory**: Display all files and subdirectories in the given directory.

## Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of Python and file operations.

## Setup and Installation

1. **Clone the repository** or download the project files to your local system.
   
2. Make sure Python is installed by running:

   ```bash
   python --version
   ```

   If Python is not installed, download and install it from [python.org](https://www.python.org/).

3. Navigate to the project directory and run the program:

   ```bash
   python file_management_system.py
   ```

## Usage

1. When you run the program, you'll see a menu with options for various file operations.
2. Input your choice (1-6) to perform the corresponding operation.

### Available Operations

- **1. Create a file**: 
   - You will be prompted to provide a directory path and a file name.
   - The program will create a new file in the specified directory.
  
- **2. Delete a file**:
   - You will be asked for the directory path and file name.
   - The program will delete the specified file or directory if it exists.
   
- **3. Copy a file**:
   - You need to provide the source directory, file name, and target directory.
   - The program will copy the file to the target directory.
   
- **4. Rename a file**:
   - Enter the directory, current file name, and the new name to rename the file.

- **5. List files in a directory**:
   - Input the directory, and the program will display all files and subdirectories inside it.

- **6. Exit**: Exit the program.

## Example Output

```
File Management System
1. Create a file
2. Delete a file or directory
3. Copy a file
4. Rename a file or directory
5. List files in a directory
6. Exit

Enter your choice: 1
Enter directory path: C:/Users/Kunal/Desktop
Enter file name: test.txt
Created file 'test.txt'.
```

## Error Handling

- **PermissionError**: If the program encounters a permissions issue (e.g., attempting to write in a protected directory), it will handle the error gracefully and display a helpful message.

- **File Already Exists**: The program checks if the file or directory already exists and prevents overwriting or deletion without confirmation.

- **Directory Not Found**: If the specified directory does not exist, the program will notify the user.

