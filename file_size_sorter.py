import os

files = os.listdir()

files = [(f, os.path.getsize(f)) for f in files if os.path.isfile(f)]

for name, size in sorted(files, key=lambda x: x[1]):
    print(name, size)
