from library.order_book_manager import OrderBookManager
from library.quote_calculator import QuoteCalculator
from library.service.response.best_price_response import BestPriceResponse


class PriceServiceBase:

    def __init__(self, api_client):
        self.order_book_manager = OrderBookManager(api_client)
        self.api_client = api_client

    def best_price(self, req):
        """
            - Öncelikle burada symbol kontrol ediliyor. Kullanıcı base ve quote değerlerini hatalı göndermiş olabilir.
              Örneğin kullanıcı ETHUSDT symbolü için, USDTETH değerini göndermiş olabilir, bu durumda doğru symbol adını
              bulmak için, symbol adının tersini alıp tekrar borsada olup olmadığına bakıyoruz, hala yoksa, symbol
              hatalıdır, hata verip requesti sonlandırıyoruz
            - OrderBookManager, daha önce bu symbolün talep edilip edilmediğini kontrol ediyor ve henüz yeni bir symbolse
              onun için socket bağlantısını kurup, orderbook'u oluşturmaya başlıyor. Burada çok fazla sayıda symbol
              gelirse, sunucudan borsaya açılabilecek socket sayısını aşabiliriz. Bunun ele alınması lazım, şimdilik
              ele alınmadı
            - İlk talep edildiğinde kullanıcıya 10 saniye sonra tekrar denemesini söylüyoruz, biz bu arada socketi başlatıp
              orderbook'u hazır ediyoruz
            - Orderbook için socket başlatılan symboller OrderBookManager sınıfında tutuluyor. Buna rağmen oradan orderbook
              elde edilemiyorsa, kodumuzda görmediğimiz bir hata vardır. Bu yönde bir uıyarı veriyoruz
        """
        real_base = req.base_currency
        real_quote = req.quote_currency

        symbol = f"{req.base_currency}{req.quote_currency}"
        if not self.api_client.is_valid_symbol(symbol):
            symbol = f"{req.quote_currency}{req.base_currency}"
            real_base = req.quote_currency
            real_quote = req.base_currency
            if not self.api_client.is_valid_symbol(symbol):
                return BestPriceResponse(False, f"Symbol {symbol} is not valid")

        ws_url = f"{self.api_client.ws_url}/{symbol}@depth"

        if not self.order_book_manager.symbol_exists(symbol):
            self.order_book_manager.create_order_book_ifnot_exists(ws_url, symbol, real_base, real_quote)
            res = BestPriceResponse(False,
                                    f"Order book for {symbol} is not ready for this pair, try again in 10 seconds")
            return res

        ob = self.order_book_manager.get_order_book(symbol)
        if ob is None:
            return BestPriceResponse(success=False,
                                     message=f"Order book for {symbol} not found, contact with the IT department")

        """
            Bu kısımda artık, orderbook hazır ve gerekli hesaplamalar için QuoteCalculator sınıfı çağrılıyor
        """
        quote_calculator = QuoteCalculator(ob)
        best_price = quote_calculator.calculate_best_price(req.action,
                                                           req.base_currency,
                                                           req.quote_currency,
                                                           float(req.amount))

        res = BestPriceResponse()
        res.set_values(best_price.total, best_price.price, best_price.currency)
        return res
