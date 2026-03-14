# file_organizer.py
import os
import shutil

def organize_folder(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            # Extract the extension (e.g., 'jpg', 'pdf')
            ext = filename.split('.')[-1].lower()
            target_folder = os.path.join(path, ext.upper())
            
            # Create folder if it doesn't exist
            os.makedirs(target_folder, exist_ok=True)
            
            # Move the file
            shutil.move(os.path.join(path, filename), os.path.join(target_folder, filename))

# Change this to your target folder path
organize_folder("./downloads")
