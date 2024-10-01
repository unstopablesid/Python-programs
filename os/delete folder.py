import os
import shutil

# Define the directories to be deleted
dirs_to_delete = ["data", "course"]

# Loop through the list of directories and delete them if they exist
for directory in dirs_to_delete:
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)
        print(f"Deleted directory: {directory}")
    else:
        print(f"Directory does not exist or is not a directory: {directory}")
