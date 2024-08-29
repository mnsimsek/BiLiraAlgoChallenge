# BiLiraAlgoChallenge

Python version 3.9

`pip install flask`  
`pip install websocket-client`  


Run `python main.py`  

Test on postman  

curl --location 'http://127.0.0.1:5000/quote' \  
--header 'Content-Type: application/json' \  
--data '{  
    "action": "sell",  
    "base_currency": "USDT",  
    "quote_currency": "BTC",  
    "amount": "2000"  
}'  
