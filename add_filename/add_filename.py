import os

directory_path = "/home/parlab/workspace_ws/custom_dataset/images"

# Ensure the directory exists
if not os.path.exists(directory_path):
    print("Directory does not exist.")
    exit(1)

# List all files in the directory
for filename in os.listdir(directory_path):
    # Check if the file is an image (you can add more image file extensions if needed)
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
        # Construct the new filename with "image" added
        new_filename = f"image_{filename}"
        # Rename the file with the new name
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
        print(f"Renamed {filename} to {new_filename}")

print("All image files renamed with 'image' added.")
