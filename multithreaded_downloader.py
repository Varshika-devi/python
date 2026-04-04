import threading
import requests

def download(url):
    filename = url.split("/")[-1]
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"Downloaded {filename}")

urls = [
    "https://example.com/file1.jpg",
    "https://example.com/file2.jpg"
]

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
