import requests

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    data = requests.get(url).json()
    print(f"{symbol} price:", data[symbol]["usd"])

if __name__ == "__main__":
    get_price("bitcoin")
