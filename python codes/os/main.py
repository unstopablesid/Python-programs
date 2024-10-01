import os

# Ensure the "data" directory exists
if not os.path.exists("data"):
    os.mkdir("data")

for i in range(10):
    old_name = f"data/Tutorial_Renamed{i+1}"
    new_name = f"data/Tutorials{i+1}"
    
    if os.path.exists(old_name) and os.path.isdir(old_name):
        os.rename(old_name, new_name)
    else:
        print(f"{old_name} does not exist or is not a directory")
