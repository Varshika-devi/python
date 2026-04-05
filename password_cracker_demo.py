import itertools

password = "123"
chars = "0123456789"

for attempt in itertools.product(chars, repeat=3):
    attempt = ''.join(attempt)
    if attempt == password:
        print("Password found:", attempt)
        break
