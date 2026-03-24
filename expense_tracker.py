total = 0

while True:
    amount = input("Enter expense (or 'q' to quit): ")

    if amount.lower() == 'q':
        break

    total += float(amount)

print("Total Expenses:", total)
