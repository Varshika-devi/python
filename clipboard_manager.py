import pyperclip

data = input("Enter text to save: ")
pyperclip.copy(data)
print("Copied to clipboard!")

print("Clipboard contains:", pyperclip.paste())
