import requests

urls = [
    "https://google.com",
    "https://github.com",
    "https://invalidsite.xyz"
]

for url in urls:
    try:
        res = requests.get(url, timeout=3)
        print(f"{url} -> {res.status_code}")
    except:
        print(f"{url} -> DOWN")
