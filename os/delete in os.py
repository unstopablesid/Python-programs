import os
import shutil

# Path to the "course" directory
course_dir = "course"

# Ensure the "course" directory exists before attempting to delete its contents
if os.path.exists(course_dir) and os.path.isdir(course_dir):
    # Loop through all the items in the directory
    for item in os.listdir(course_dir):
        item_path = os.path.join(course_dir, item)
        # Check if it is a file
        if os.path.isfile(item_path):
            os.remove(item_path)
        # Check if it is a directory
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    print("All files and folders in 'course' have been deleted.")
else:
    print(f"'{course_dir}' does not exist or is not a directory.")
