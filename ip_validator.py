ip = input("Enter IP address: ")

parts = ip.split(".")

if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
    print("Valid IP address")
else:
    print("Invalid IP address")
