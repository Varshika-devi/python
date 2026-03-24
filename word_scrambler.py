import random

word = input("Enter a word: ")

scrambled = ''.join(random.sample(word, len(word)))

print("Scrambled word:", scrambled)
