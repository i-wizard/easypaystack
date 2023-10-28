from easypaystack.config import PackageConfig
from easypaystack.helper import amount_validator

class Payment(PackageConfig):
    def initiate_payment(self, email: str, kobo_amount: int, reference, channels: list=None) -> dict:
        """

        Args:
            email: email of the user making the payment.
            kobo_amount: payment amount * 100 (amount must be in kobo)
            reference: a unique reference for this transaction
            channels: Accepted channels to perform this payment. Enum['card', 'bank', 'ussd', 'qr', 'mobile_money', 'bank_transfer']
                    If no channel is sent all channels are used by default

        Returns:
            {'status': 200,
            'data': {
                'status': 200, 
                'data': {
                    'status': True, 'message': 'Authorization URL created', 
                    'data': {
                        'authorization_url': 'https://checkout.paystack.com/e23vsfdgw2w4q7', 'access_code': 'e23vsfdgw2w4q7', 'reference': 'uniquers453'
                        }
                    }
                }
            }

        context:
            This method initiates a payment and returns a valid
            payment reference and a payment link.
            The payment link can be used directly by pasting into a web browser.
            The payent link is useful if there is not frontend app to utilize the reference

        """
        #TODO: Specify types of error raised
        _url = self.parse_url("transaction/initialize")
        kobo_amount = amount_validator(kobo_amount)
        payload = {
            "email":email,
            "amount":kobo_amount,
            "reference":reference
        }
        channels and isinstance(channels, list) and payload.update({"channels":channels})
        response = self.handle_request("POST", _url, payload)
        return response

    def charge_authorization(self, authorization_code: str, email: str, kobo_amount: int, reference: str) -> dict:
        """

        Args:
            email: email of the user making the payment.
            kobo_amount: payment amount * 100 (amount must be in kobo)
            reference: a unique reference for this transaction
            authorization_code: This the authorization code gotten when the user's card was tokenized

        Returns:
            {
            'status': 200, 
            'data': {
                'status': 200, 
                'data': {
                    'status': True, 
                    'message': 'Charge attempted', 
                    'data': {
                        'amount': 800090, 
                        'currency': 'NGN', 
                        'transaction_date': '2023-10-28T22:47:47.000Z', 
                        'status': 'success', 
                        'reference': 'uniqueref213david971', 
                        'domain': 'test', 
                        'metadata': '', 
                        'gateway_response': 'Approved', 
                        'message': None, 
                        'channel': 'card', 
                        'ip_address': None, 
                        'log': None, 
                        'fees': 22002, 
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
                        'id': 3233869359
                    }
                }
            }
        }
 

        context:
            This method debits a user's card, it's a one step process.
            Ensure the email sent is the same one used when tokenizing the card.

        """
        _url = self.parse_url("transaction/charge_authorization")
        kobo_amount = amount_validator(kobo_amount)
        payload = {
            "email":email,
            "amount":kobo_amount,
            "reference":reference,
            "authorization_code":authorization_code
        }
        response = self.handle_request("POST", _url, payload)
        return response