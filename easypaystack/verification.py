from easypaystack.config import PackageConfig
from easypaystack.error_handler import *

class PaystackVerification(PackageConfig):

    def resolve_account(self, account: str=None, bank_code: str=None):
        _url = self.parse_url(f'bank/resolve?account_number={account}&bank_code={bank_code}')
        response = self.handle_request("GET", _url)
        return response

    def verify_payment(self, reference):
        """
        Args:
            reference: The unique reference used to initiate this transaction
        Returns:
            {
                'status': 200,
                'data': {
                    'status': 200,
                    'data': {
                        'status': True,
                        'message': 'Verification successful',
                        'data': {
                            'id': 3233860693,
                            'domain': 'test',
                            'status': 'success',
                            'reference': 'uniquers453',
                            'receipt_number': None,
                            'amount': 5000,
                            'message': None,
                            'gateway_response': 'Successful',
                            'paid_at': '2023-10-28T22:43:00.000Z',
                            'created_at': '2023-10-28T22:39:45.000Z',
                            'channel': 'card',
                            'currency': 'NGN',
                            'ip_address': '102.223.1.241',
                            'metadata': '',
                            'log': {
                                'start_time': 1698532977,
                                'time_spent': 3,
                                'attempts': 1,
                                'errors': 0,
                                'success': True,
                                'mobile': False,
                                'input': [],
                                'history': [
                                    {
                                        'type': 'action',
                                        'message': 'Attempted to pay with card',
                                        'time': 3
                                    },
                                    {
                                        'type': 'success',
                                        'message': 'Successfully paid with card',
                                        'time': 3
                                    }
                                ]
                            },
                            'fees': 75,
                            'fees_split': None,
                            'authorization': {
                                'authorization_code': 'AUTH_y3ttenw9mb',
                                'bin': '408408',
                                'last4': '4081',
                                'exp_month': '12',
                                'exp_year': '2030',
                                'channel': 'card',
                                'card_type': 'visa ',
                                'bank': 'TEST BANK',
                                'country_code': 'NG',
                                'brand': 'visa',
                                'reusable': True,
                                'signature': 'SIG_v7384U8nn6yD0UhXmLdE',
                                'account_name': None
                            },
                            'customer': {
                                'id': 146083267,
                                'first_name': None,
                                'last_name': None,
                                'email': 'david@gmail.com',
                                'customer_code': 'CUS_hsm5lloajff2c13',
                                'phone': None,
                                'metadata': None,
                                'risk_action': 'default',
                                'international_format_phone': None
                            },
                            'plan': None,
                            'split': {},
                            'order_id': None,
                            'paidAt': '2023-10-28T22:43:00.000Z',
                            'createdAt': '2023-10-28T22:39:45.000Z',
                            'requested_amount': 5000,
                            'pos_transaction_data': None,
                            'source': None,
                            'fees_breakdown': None,
                            'transaction_date': '2023-10-28T22:39:45.000Z',
                            'plan_object': {},
                            'subaccount': {}
                        }
                    }
                }
            }
        context:
            This returns the current status of a transaction
            The transaction could be successful, failed or abandoned

        """
        _url = self.parse_url(f'transaction/verify/{reference}')
        response = self.handle_request("GET", _url)
        return response
    

    def verify_transfer(self, reference: str=None):
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