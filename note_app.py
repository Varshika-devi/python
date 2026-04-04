FILE = "notes.txt"

def add_note(note):
    with open(FILE, "a") as f:
        f.write(note + "\n")

def view_notes():
    with open(FILE, "r") as f:
        print(f.read())

if __name__ == "__main__":
    choice = input("1.Add 2.View: ")
    
    if choice == "1":
        note = input("Enter note: ")
        add_note(note)
    else:
        view_notes()
