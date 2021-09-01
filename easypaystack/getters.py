from easypaystack.config import PackageConfig
from easypaystack.error_handler import *

class Getters(PackageConfig):
    def get_banks(self, country="nigeria", perPage=50, currency='NGN'):
        _url = self.parse_url(f'bank?country={country}&currency={currency}&perpage={perPage}')
        response = self.handle_request("GET", _url, )
        return response