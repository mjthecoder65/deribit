import requests

class Client:
    def __init__(self, apikey, secret):
        self.apikey = apikey
        self.secret = secret
        self.baseurl = "https://www.deribit.com"

    def get_account_info(self):
        pass

    def get_deposits(self):
        pass

    def get_transfers(self):
        pass

    def withdraw(self):
        pass

    def cancel_withdraw(self):
        pass

    def cancel_transfer_by_id(self, id):
        pass

    def submit_tranfer_to_user(self):
        pass

    def sumit_transfer_to_subaccount(self):
        pass
    

    def buy(self):
        pass

    def sell(self):
        pass

    def get_book_summary(self):
        pass

    def get_auth_token(self):
        pass

    def logout(self):
        pass


__all__ = ["Client"]