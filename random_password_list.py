import random
import string

num = int(input("How many passwords? "))
length = int(input("Password length: "))

chars = string.ascii_letters + string.digits

for _ in range(num):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
