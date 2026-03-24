import random

while True:
    roll = input("Roll dice? (y/n): ")

    if roll.lower() == 'y':
        print("You got:", random.randint(1, 6))
    else:
        break
