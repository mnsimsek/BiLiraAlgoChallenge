import json
import re

from flask import Flask, request, jsonify
from library.service.binance_price_service import BinancePriceService
from library.service.request.best_price_request import BestPriceRequest

app = Flask(__name__)
service = BinancePriceService()


@app.route('/quote', methods=['POST'])
def quote():

    try:

        data = request.get_json()

        if not data or 'action' not in data or 'base_currency' not in data or 'quote_currency' not in data or 'amount' not in data:
            return jsonify({"error": "Invalid request format"}), 400

        action = data['action'].lower()
        base_currency = data['base_currency'].lower()
        quote_currency = data['quote_currency'].lower()
        amount = data['amount']

        if action != "buy" and action != "sell":
            return jsonify({"error": "Invalid action"}), 400
        if base_currency == "":
            return jsonify({"error": "Invalid base currency"}), 400
        if quote_currency == "":
            return jsonify({"error": "Invalid quote currency"}), 400

        req = BestPriceRequest(action, base_currency, quote_currency, amount)
        res = service.best_price(req)

        json_res = json.dumps(res.__dict__)

        return jsonify(json_res)

    except Exception as e:
        return jsonify({"error": "Unexpected error!.. Contact system administrator"}), 500


if __name__ == '__main__':
    app.run(debug=True)

'''
import time
from library.service.binance_price_service import BinancePriceService
from library.service.request.best_price_request import BestPriceRequest

if __name__ == "__main__":
    price_service = BinancePriceService()

    while True:



        action = "buy"
        base_currency = "USDT"
        quote_currency = "ETH"
        amount = 500

        base_currency = base_currency.lower()
        quote_currency = quote_currency.lower()

        req = BestPriceRequest(action, base_currency, quote_currency, amount)
        res = price_service.best_price(req)

        if res.success:
            print(f"{res.currency} - {res.total} - {res.price}");
        else:
            print(res.message)

        time.sleep(5)

'''
