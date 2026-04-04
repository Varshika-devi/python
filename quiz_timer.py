import time

questions = {
    "2+2": "4",
    "3+5": "8"
}

score = 0

for q, ans in questions.items():
    print(q)
    start = time.time()
    
    user = input("Answer: ")
    end = time.time()

    if end - start > 5:
        print("Too slow!")
    elif user == ans:
        score += 1

print("Score:", score)
