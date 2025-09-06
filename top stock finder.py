import heapq
import requests
top_stocks_heap = []
max_size = 5


def fetch_stock_data():
    url = "https://stock.indianapi.in/ipo"
    headers = {"X-Api-Key": "sk-live-a9FAre1i6O2NkL9rY5Nyp68a0kYZ4yOim4KwGTyO"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['upcoming']


def process_stocks(stocks):
    for stock in stocks:
        price = stock.get('max_price')
        if price is None:
            price = stock.get('min_price')
        if price is None:
            continue

        symbol = stock.get('symbol', 'Unknown')

        if len(top_stocks_heap) < max_size:
            heapq.heappush(top_stocks_heap, (price, symbol))
        else:
            if price > top_stocks_heap[0][0]:
                heapq.heapreplace(top_stocks_heap, (price, symbol))


def display_top_stocks():

    sorted_stocks = sorted(top_stocks_heap, reverse=True)
    for price, symbol in sorted_stocks:
        print(f"{symbol}: ₹{price}")


stocks_data = fetch_stock_data()
process_stocks(stocks_data)
display_top_stocks()
