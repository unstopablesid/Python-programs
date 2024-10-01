import os

# Create the "course" directory
course_dir = "course"
if not os.path.exists(course_dir):
    os.mkdir(course_dir)

# Create 10 subfolders named "tutorial1" to "tutorial10" within the "course" directory
for i in range(1, 11):
    tutorial_dir = os.path.join(course_dir, f"tutorial{i}")
    if not os.path.exists(tutorial_dir):
        os.mkdir(tutorial_dir)

print("Course directory with 10 tutorial subfolders created successfully.")
