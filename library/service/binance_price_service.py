from library.exchange.binance_api_client import BinanceApiClient
from library.service.price_service_base import PriceServiceBase


class BinancePriceService(PriceServiceBase):

    def __init__(self):
        super().__init__(BinanceApiClient())


