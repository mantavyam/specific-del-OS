import os

def delete_files(folder):
    deleted_files = []
    file_count_before = 0
    file_count_after = 0

    # Count files before deletion
    for _, _, files in os.walk(folder):
        file_count_before += len(files)

    # Delete files with specified extensions and count remaining files
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.txt') or file_path.endswith('.json.xz'):
                deleted_files.append(file_path)
                os.remove(file_path)
            else:
                file_count_after += 1

    # Print deleted file names and count of files after deletion
    print("Deleted files:")
    for deleted_file in deleted_files:
        print(deleted_file)
    print("Total files before deletion:", file_count_before)
    print("Total files after deletion:", file_count_after)

def main():
    main_folder = input("Enter the path of the main folder: ")
    
    if os.path.exists(main_folder):
        for root, dirs, _ in os.walk(main_folder):
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                print("\nProcessing folder:", folder_path)
                delete_files(folder_path)
    else:
        print("The specified main folder does not exist.")

if __name__ == "__main__":
    main()
