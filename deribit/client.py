import requests

class Client:
    def __init__(self, apikey, secret):
        self.apikey = apikey
        self.secret = secret



__all__ = ["Client"]