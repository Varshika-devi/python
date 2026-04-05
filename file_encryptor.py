key = 123

with open("sample.txt", "rb") as f:
    data = f.read()

encrypted = bytes([b ^ key for b in data])

with open("encrypted.bin", "wb") as f:
    f.write(encrypted)

print("File encrypted!")
