tasks = []

while True:
    task = input("Enter a task (or 'quit' to stop): ")
    if task.lower() == "quit":
        break
    tasks.append(task)

print("Your tasks:")
for t in tasks:
    print("-", t)
