from abc import ABC, abstractmethod


class SocketFeedable(ABC):
    """
        Eğer bir sınıf socketten gelen(WebSocketClient sınıfı) verilerle besleniyorsa, bu sınıfı inherit edip
        abstract metodları override etmek durumundadır. Örneğin OrderBook sınıfı, socketten gelen bids ve asks
        verileriyle besleniyor, bu sebeple OrderBook sınıfı SocketFeedable sınıfından inherit edilmiştir
    """

    @abstractmethod
    def on_message(self, ws, message, api_client):
        pass
