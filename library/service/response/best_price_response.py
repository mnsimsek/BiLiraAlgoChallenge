from library.service.response.response_base import ResponseBase


class BestPriceResponse(ResponseBase):
    total = 0
    price = 0
    currency = ""

    def __init__(self, success=True, message=""):
        ResponseBase.__init__(self, success, message)

    def set_values(self, total, price, currency):
        self.total = total
        self.price = price
        self.currency = currency
