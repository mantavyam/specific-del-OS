## specific-del-OS
# Folder Cleanup Tool
This Python script is designed to efficiently clean up files within a specified main folder and its subfolders on your local machine. It traverses through all subfolders within the main folder, counts the number of files, deletes files with specific file extensions (e.g., '.txt' or '.json.xz'), and provides a summary of the deletion operation.

# Features
Recursively scans through all subfolders within the main folder.
Counts the total number of files in each subfolder before and after deletion.
Deletes files with specified extensions ('.txt' or '.json.xz').
Provides a list of deleted file names.
Displays the count of files before and after the deletion operation.
# Usage
Clone or download this repository to your local machine.
Ensure you have Python installed on your system.
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script by executing the command python folder_cleanup.py.
Enter the path of the main folder when prompted.
The script will process each subfolder within the main folder, delete specified files, and provide the deletion summary.

# Example
Suppose you have a main folder named data containing several subfolders, each with various files. Running this script on the data folder will clean up files with the extensions '.txt' or '.json.xz' within each subfolder, providing details of the deleted files and the count of files before and after the deletion operation.

# Note
This script permanently deletes files with the specified extensions. Exercise caution when using it.
Ensure you provide the correct path to the main folder to avoid unintended deletions.
Feel free to contribute, report issues, or suggest improvements!
