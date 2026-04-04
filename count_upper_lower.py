text = input("Enter text: ")

upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())

print("Uppercase:", upper)
print("Lowercase:", lower)
