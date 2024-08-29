import requests
from library.exchange.api_client_base import ApiClientBase


class KucoinApiClient(ApiClientBase):
    """
        Kucoin entegre edilmek istendiğinde bu sınıfın doldurulması yeterlidir. Sistemin diğer parçalarına ekleme yapmak gerekmiyor
    """
    def __init__(self):
        super().__init__("...")

    def is_valid_symbol(self, symbol):
        pass

    def parse_partial_book_depth_stream(self, data):
        pass
