import threading
import time
import websocket


class WebSocketClient:

    def __init__(self, socket_feedable, api_client, ws_url):
        self.socket_feedable = socket_feedable
        self.api_client = api_client
        self.ws_url = ws_url

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")
        print(f"Url: { self.ws_url}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocketnetwork closed")
        print(f"Status: {close_status_code}, Message: {close_msg}")
        print(f"Url: { self.ws_url}")

    def on_open(self, ws):
        print("WebSocketnetwork opened")
        print(f"Url: { self.ws_url}")

    def start_async(self):
        wst = threading.Thread(target=self.start)
        wst.daemon = True
        wst.start()

    def on_message(self, ws, message):
        self.socket_feedable.on_message(ws, message, self.api_client)

    def start(self):
        """
            Hata vermesi durumunda 5sn bekleyip tekrardan bağlantıyı kurmaya çalışıyor
        """
        while True:
            try:
                ws = websocket.WebSocketApp(self.ws_url,
                                            on_open=self.on_open,
                                            on_message=self.on_message,
                                            on_error=self.on_error,
                                            on_close=self.on_close)

                ws.run_forever()
            except Exception as e:
                print(f"Exception: {e}")
                print("Reconnecting in 5 seconds...")
                time.sleep(5)
