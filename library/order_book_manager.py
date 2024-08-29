from library.network.web_socket_client import WebSocketClient
from library.order_book import OrderBook
import threading


class OrderBookManager:
    lock = threading.Lock()

    def __init__(self, api_client):
        self.symbols = {}
        self.api_client = api_client

    def symbol_exists(self, symbol):
        return symbol in self.symbols

    def create_order_book_ifnot_exists(self, ws_url, symbol, base_currency, quote_currency):
        """
            Orderbook oluşturulurken yeni bir talepo daha gelebilir, bu durumda aynı kodun iki kere çalışmasını
            istemiyoruz, iki kere socket oluşturma durumu ortaya çıkabilir. Bu sebeple burada lock'lama mekanizması
            kullandık
        """
        with self.lock:
            if not self.symbol_exists(symbol):
                ob = OrderBook(symbol, base_currency, quote_currency)
                wsc = WebSocketClient(ob, self.api_client, ws_url)
                wsc.start_async()
                self.symbols[symbol] = ob

    def get_order_book(self, symbol):
        if self.symbol_exists(symbol):
            return self.symbols[symbol]
        else:
            return None
