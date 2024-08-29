from library.exchange.binance_api_client import BinanceApiClient
from library.exchange.bingx_api_client import BingXApiClient
from library.quote_calculator import QuoteCalculator
from library.service.price_service_base import PriceServiceBase
from library.service.response.best_price_response import BestPriceResponse


class BingXPriceService(PriceServiceBase):
    def __init__(self):
        super().__init__(BingXApiClient())

