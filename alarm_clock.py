import time

alarm_time = input("Set time (HH:MM:SS): ")

while True:
    current = time.strftime("%H:%M:%S")
    if current == alarm_time:
        print("Wake up!")
        break
