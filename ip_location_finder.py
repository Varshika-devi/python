import requests

ip = input("Enter IP: ")
res = requests.get(f"http://ip-api.com/json/{ip}")
data = res.json()

print("Country:", data['country'])
print("City:", data['city'])
