text = input("Enter a string: ")
count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

print("Character counts:", count)
