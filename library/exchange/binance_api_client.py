import requests
from library.exchange.api_client_base import ApiClientBase


class BinanceApiClient(ApiClientBase):

    def __init__(self):
        super().__init__("https://api.binance.com/api/v3/exchangeInfo", "wss://stream.binance.com:9443/ws")

    def is_valid_symbol(self, symbol):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            symbols = [s['symbol'] for s in data['symbols']]
            return symbol.upper() in symbols
        except Exception as e:
            print(f"Error fetching symbols: {e}")
            return False

    def parse_partial_book_depth_stream(self, data):

        orders = {"bids": {}, "asks": {}}

        if 'b' in data and 'a' in data:

            orders["bids"] = {}
            for bid in data['b']:
                price, quantity = bid
                if float(quantity) == 0.0:
                    orders["bids"].pop(price, None)
                else:
                    orders["bids"][price] = float(quantity)

            orders["asks"] = {}
            for ask in data['a']:
                price, quantity = ask
                if float(quantity) == 0.0:
                    orders["asks"].pop(price, None)
                else:
                    orders["asks"][price] = float(quantity)

        return orders
