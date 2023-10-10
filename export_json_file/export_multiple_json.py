import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import threading

def run_labelme_export_json(file_path):
    command = ["labelme_export_json", file_path]
    try:
        subprocess.run(command, check=True)
        status_label.config(text=f"Exported: {file_path}")
    except subprocess.CalledProcessError as e:
        status_label.config(text=f"Error exporting {file_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_file_path = os.path.join(root, file)
                image_file_path = json_file_path.replace(".json", ".jpg")
                if os.path.exists(image_file_path):
                    run_labelme_export_json(json_file_path)
                else:
                    status_label.config(text=f"Image file not found: {image_file_path}")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        status_label.config(text="Processing...")
        threading.Thread(target=process_directory, args=(directory,)).start()

# Create the main application window
root = tk.Tk()
root.title("LabelMe Export JSON Runner")

# Create and configure GUI elements
browse_button = tk.Button(root, text="Browse Directory", command=browse_directory)
status_label = tk.Label(root, text="", wraplength=400)

# Place GUI elements in the window
browse_button.pack(pady=10)
status_label.pack()

# Start the GUI event loop
root.mainloop()
