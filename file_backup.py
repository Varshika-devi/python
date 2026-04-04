import os
import shutil

def backup(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for file in os.listdir(src):
        full_path = os.path.join(src, file)
        if os.path.isfile(full_path):
            shutil.copy(full_path, dest)
            print(f"Copied {file}")

if __name__ == "__main__":
    source = input("Source folder: ")
    destination = input("Backup folder: ")
    backup(source, destination)
