low = 1
high = 100

print("Think of a number between 1 and 100.")

while True:
    guess = (low + high) // 2
    print("Is it", guess, "?")

    feedback = input("Enter 'high', 'low', or 'correct': ")

    if feedback == "correct":
        print("Yay! I guessed it!")
        break
    elif feedback == "high":
        high = guess - 1
    elif feedback == "low":
        low = guess + 1
