class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

students = []

def add_student():
    name = input("Name: ")
    marks = int(input("Marks: "))
    students.append(Student(name, marks))

def show_students():
    for s in students:
        s.display()

if __name__ == "__main__":
    while True:
        ch = input("1.Add 2.Show 3.Exit: ")
        if ch == "1":
            add_student()
        elif ch == "2":
            show_students()
        else:
            break
