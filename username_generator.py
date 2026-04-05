import random

names = ["alex", "sam", "john", "leo"]
numbers = random.randint(100, 999)

username = random.choice(names) + str(numbers)

print("Generated username:", username)
