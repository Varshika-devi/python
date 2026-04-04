numbers = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three",
    4: "Four", 5: "Five"
}

num = int(input("Enter number (0-5): "))
print(numbers.get(num, "Not supported"))
