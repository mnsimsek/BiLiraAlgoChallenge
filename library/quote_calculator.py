from library.entity.best_price import BestPrice


class QuoteCalculator:

    def __init__(self, order_book):
        self.order_book = order_book

    def calculate_best_price(self, action, base_currency, quote_currency, amount):
        total_base = 0
        total_quote = 0

        order_type = "asks" if action == "buy" else "bids"
        prices = list(self.order_book.orders[order_type].keys())
        orders = self.order_book.orders[order_type]

        if base_currency == self.order_book.base_currency:
            total_base = amount
            for price in prices:
                order_amount = orders[price]
                required_amount = order_amount if amount >= order_amount else amount
                amount = amount - required_amount
                total_quote += required_amount * float(price)
                if amount <= 0:
                    break
        else:
            total_quote = amount
            for price in prices:
                order_amount = orders[price]
                required_amount = order_amount * float(price) if amount >= order_amount * float(price) else amount
                amount = amount - required_amount
                total_base += required_amount / float(price)
                if amount <= 0:
                    break

        ''' 
        Amount değerinin çok yüksek olması durumunda(Yani order book'ta karşılayacak miktar yoksa)
        Olduğu kadar üzerinden hesaplama yapıyor. Eğer bu durum gerçekleşiyorsa, kod buraya geldiğinde amount değeri
        0'dan büyük olur. Bu durumda da total değerden çıkarıyoruz        
        '''
        if amount > 0:
            if base_currency == self.order_book.base_currency:
                total_base -= amount
            else:
                total_quote -= amount

        price = total_quote / total_base
        total = total_quote if base_currency == self.order_book.base_currency else total_base
        currency = quote_currency

        return BestPrice(total, price, currency)
