class BestPriceRequest:
    def __init__(self, action, base_currency, quote_currency, amount):
        self.action = action
        self.base_currency = base_currency
        self.quote_currency = quote_currency
        self.amount = amount
