import requests

from easypaystack.error_handler import *


class PackageConfig():
    base_url = 'https://api.paystack.co/'

    def __init__(self, secret_key: str=None):
        if secret_key is None:
            raise AuthKeyError("Missing paystack secret key")
        self.secret_key = secret_key
        self.headers = {
            'Authorization': f'Bearer {self.secret_key}',
            'user-agent': "easy-python-paystack",
            "Content-Type": "Application/json"
        }

    def parse_url(self, path):
        return f'{self.base_url}{path}'

    def parse_response(self, response):
        data = response.json()
        return {"status":response.status_code, "data": data}

    def handle_request(self, method, url, data=None):
        request_map = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete
        }
        request = request_map.get(method)
        if not request:
            raise RequestMethodError('This method is currently not available')
        response = request(url, headers=self.headers, json=data)
        if f'{response.status_code}'.startswith('2'):
            final_response = self.parse_response(response)
        else:
            final_response = response.json()
        return {"status":response.status_code, "data":final_response}
