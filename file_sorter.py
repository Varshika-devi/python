import os
import shutil

def organize(folder):
    for file in os.listdir(folder):
        ext = file.split(".")[-1]
        new_folder = os.path.join(folder, ext)

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        shutil.move(os.path.join(folder, file), new_folder)

if __name__ == "__main__":
    organize("test_folder")
