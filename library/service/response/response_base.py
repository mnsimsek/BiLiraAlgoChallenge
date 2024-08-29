class ResponseBase:
    def __init__(self, success=True, message=""):
        self.success = success
        self.message = message
