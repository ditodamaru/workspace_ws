import os
import shutil

source_directory = "/home/parlab/workspace_ws/rgb_day2"  # Change this to your source directory
target_directory = "/home/parlab/workspace_ws/custom_dataset/labels"

# Function to copy label.png files from subdirectories to the target directory
def copy_label_files(source_dir, target_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file == "label.png":
                folder_name = os.path.basename(root)
                suffix = folder_name.replace("/", "_")  # Replace slashes with underscores
                new_filename = f"label{suffix}.png"
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, new_filename)
                shutil.copy(source_path, target_path)
                print(f"Copied {source_path} to {target_path}")

copy_label_files(source_directory, target_directory)
