import time

sentence = "Python is fun to learn"
print(sentence)

start = time.time()
typed = input("Type above: ")
end = time.time()

print("Time taken:", end - start, "seconds")
