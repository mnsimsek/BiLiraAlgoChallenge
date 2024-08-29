from abc import ABC, abstractmethod


class ApiClientBase(ABC):
    """
        Sisteme entegre edilecek tüm borsalar bu sınıftan inherit edilecek. rest çağrıları ve websocket bağplantıları için
        url bilgileri bu sınıfa parametere olarak iletilmeli
    """

    def __init__(self, api_url, ws_url):
        self.api_url = api_url
        self.ws_url = ws_url

    @abstractmethod
    def is_valid_symbol(self, symbol):
        """
            Verilen bir symbolün borsada olup olmadığını döndürüyor
        """
        pass


    @abstractmethod
    def parse_partial_book_depth_stream(self, data):
        """
            Her borsanın api sistemi farklı, socketten gelen orderbook verilerinin formatı farklı farklı.
            Bu metod her bir borsa sınıfı tarafından override edilip, gerekli düzenleme işlemi gerçekleştirilecek
        """
        pass
