from library.exchange.kucoin_api_client import KucoinApiClient
from library.service.price_service_base import PriceServiceBase


class KucoinPriceService(PriceServiceBase):
    def __init__(self):
        super().__init__(KucoinApiClient())

