filename = input("Enter file name: ")
word = input("Enter word to search: ")

with open(filename, "r") as file:
    for line_num, line in enumerate(file, 1):
        if word in line:
            print(f"Line {line_num}: {line.strip()}")
