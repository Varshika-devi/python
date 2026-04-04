def encrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) + key)
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) - key)
    return result

if __name__ == "__main__":
    msg = input("Message: ")
    key = int(input("Key: "))
    
    enc = encrypt(msg, key)
    print("Encrypted:", enc)
    print("Decrypted:", decrypt(enc, key))
