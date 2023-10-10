import os
import tkinter as tk
from tkinter import filedialog

def remove_word_from_filenames(directory_path, word_to_remove):
    try:
        for filename in os.listdir(directory_path):
            if word_to_remove in filename:
                new_filename = filename.replace(word_to_remove, "")
                os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
        status_label.config(text="Word removed from filenames")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def browse_directory():
    directory_path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory_path)

def remove_word_from_filenames_button():
    directory_path = directory_entry.get()
    word_to_remove = word_to_remove_entry.get()
    remove_word_from_filenames(directory_path, word_to_remove)

# Create the main window
root = tk.Tk()
root.title("Remove Word from Filenames")

# Create and configure the frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Directory selection
directory_label = tk.Label(frame, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(frame)
directory_entry.pack()
browse_button = tk.Button(frame, text="Browse", command=browse_directory)
browse_button.pack()

# Word to remove
word_to_remove_label = tk.Label(frame, text="Word to Remove:")
word_to_remove_label.pack()
word_to_remove_entry = tk.Entry(frame)
word_to_remove_entry.pack()

# Remove word button
remove_button = tk.Button(frame, text="Remove Word from Filenames", command=remove_word_from_filenames_button)
remove_button.pack()

# Status label
status_label = tk.Label(frame, text="")
status_label.pack()

# Start the GUI main loop
root.mainloop()
