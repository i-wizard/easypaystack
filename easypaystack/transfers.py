from easypaystack.error_handler import InputError
from easypaystack.config import PackageConfig
from easypaystack.helper import amount_validator


class Transfer(PackageConfig):

    def create_recipient(self, name: str=None, account_number: str=None, bank_code: str=None):
        _url = self.parse_url('transferrecipient')
        payload = {
            "account_number": account_number,
            "bank_code": bank_code,
            "name": name,
            "type": "nuban",
            "currency": "NGN"
        }
        response = self.handle_request("POST", _url, payload)
        return response

    def initiate_transfer(self, recipient_code: str=None, amount: int=None, narration: str=None):
        amount = amount_validator(amount)
        _url = self.parse_url('transfer')
        payload = {
            "source": 'balance',
            "amount": amount,
            'recipient': recipient_code,
            'reason': narration
        }
        response = self.handle_request("POST", _url, payload)
        return response

    def get_balance(self):
        _url = self.parse_url('balance')
        return self.handle_request("GET", _url)

    def get_transfer_recipients(self, perPage: int=50, page: int=1, start=None, end=None):
        _url = self.parse_url(f'transferrecipient?perPage={perPage}&page={page}')
        return self.handle_request("GET", _url)

    def get_single_transfer_recipient(self, recipient_code: str=None):
        if not recipient_code:
            raise InputError('Recipient code is needed to complete this request')
        _url = self.parse_url(f'transferrecipient/{recipient_code}')
        return self.handle_request("GET", _url)
    
    def update_transfer_recipient(self, recipient_code: str=None, email: str=None, name: str=None, description: str=None):
        if not recipient_code or not name or not email:
            raise InputError("Recipient code or id, email and name is required to process this request.")
        _url = self.parse_url(f'transferrecipient/{recipient_code}')
        payload = {
            "name":name,
            "email":email,
            'description':description
        }
        return self.handle_request("PUT", _url,  payload)
    
    def delete_transfer_recipient(self, recipient_code=None):
        if not recipient_code:
            raise InputError('Recipient code is needed to complete this request')
        _url = self.parse_url(f'transferrecipient/{recipient_code}')
        return self.handle_request("DELETE", _url)
    
    def get_transfers(self, perPage=50, page=1):
       _url = self.parse_url(f'transfer?perPage={perPage}&page={page}')
       return self.handle_request("GET", _url)
