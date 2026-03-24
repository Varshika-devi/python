contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == "3":
        break
    else:
        print("Invalid choice")
