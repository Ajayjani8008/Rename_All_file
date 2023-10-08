import os

def rename_all_files(filepath, extension,startingname):
    try:
        files = os.listdir(filepath)
        renamed_count = 0
        for index, filename in enumerate(files, start=1):
            if filename.endswith(extension):
                new_filename = f"{startingname}{index}.jpg"
                os.rename(
                    os.path.join(filepath, filename),
                    os.path.join(filepath, new_filename),
                )
                renamed_count += 1
            else:
                print(f"Skipping file: {filename} (Invalid extension)")
        
        if renamed_count > 0:
            print(f"Renamed {renamed_count} file(s) with '{extension}' extension to '{startingname}{index}.jpg'.")
        else:
            print(f"No files with '{extension}' extension found for renaming.")
    except FileNotFoundError:
        print("Invalid path. Please enter a valid file path.")

print("Attention: This program will rename files in the specified directory.")
print("Make sure to enter the full path carefully!")
filepath = input("Enter directory(folder) path: ")
extension = input("Enter the file extension you want to rename (like as  .png .jpg ...): ")
startingname=input("Enter starting name of the file: ")
rename_all_files(filepath, extension,startingname)
