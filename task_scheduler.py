import time

def task():
    print("Task executed!")

while True:
    print("Waiting...")
    time.sleep(5)  # runs every 5 seconds
    task()
