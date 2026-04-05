import requests

url = input("Image URL: ")
img = requests.get(url)

with open("downloaded.jpg", "wb") as f:
    f.write(img.content)

print("Image downloaded!")
