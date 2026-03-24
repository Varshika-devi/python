score = 0

print("Welcome to Quiz Game!")

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("5 + 3 = ")
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your final score is:", score)
