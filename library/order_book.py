import json
from library.network.socket_feedable import SocketFeedable


class OrderBook(SocketFeedable):
    """
        Socketten gelen verilerle orderbook yenileniyor.
    """
    def __init__(self, symbol, base_currency, quote_currency):
        self.symbol = symbol
        self.base_currency = base_currency
        self.quote_currency = quote_currency
        self.orders = {"bids": {}, "asks": {}}

    def on_message(self, ws, message, api_client):
        data = json.loads(message)
        self.orders = api_client.parse_partial_book_depth_stream(data)

