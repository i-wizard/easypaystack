from easypaystack.config import PackageConfig
from easypaystack.error_handler import *

class PaystackVerification(PackageConfig):

    def resolve_account(self, account=None, bank_code=None):
        _url = self.parse_url(f'bank/resolve?account_number={account}&bank_code={bank_code}')
        response = self.handle_request("GET", _url)
        return response

    def verify_payment(self, reference):
        _url = self.parse_url(f'transaction/verify/{reference}')
        response = self.handle_request("GET", _url)
        return response
    

    def verify_transfer(self, reference=None):
        if reference is None:
            raise ValueError("Transfer reference is needed to process this request")
        _url = self.parse_url(f'transfer/verify/{reference}')
        response = self.handle_request("GET", _url)
        return response

    def resolve_card_bin(self, six_digit=''):
        if len(six_digit) != 6:
            raise ValueError('Card digits must be only the first six digits')
        _url = self.parse_url(f'decision/bin/{six_digit}')
        response = self.handle_request("GET", _url)
        return response