import pyshorteners

url = input("Enter URL: ")

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print("Shortened URL:", short_url)
