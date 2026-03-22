num = int(input("Enter a number: "))
digits = str(num)
total = sum(int(d)**len(digits) for d in digits)

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
