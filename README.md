# Overview
This package is aimed at helping developers interact with the paystack api easily and quickly too👌.

# Installation
Create and activate your virtual environment.
```
pip install easypaystack
```
You can also add this dependency to your requirements file.

```
pip freeze > requirements.txt
```

# Usage
Alright let's get down to business

Every call made will return a python dictionary containing a status code(2xx, 4xx)  and a **data** object.

##### Resolve Account Number
```py
from easypaystack.verification import PaystackVerification
```
```py
paystack = PaystackVerification(secret_key)
response = paystack.resolve_account(account_number, bank_code)
```

**NOTE** whenever you import any class from the easypaystack sdk, always instantiate it with your secret key else it will raise a "MissinAuthKeyError"
*Remember to never include your **secret key** ❌ in your code, instead use environment variables like the example below*.
```py
from decouple import config

paystack = PaystackVerification(config("PAYSTACK_SECRET"))
```
### Verify Payment
```py
response = paystack.verify_payment(reference=payment_reference)
```

### Create Recipient
In order to do a transfer with paystack you need to first create a the transfer recipient.
```py
from easypaystack.transfers import Transfer

paystack = Transfer(secret_key)
response = paystack.create_recipient(name="John Doe", account_number="07*******", bank_code="035")
```

### Get All Transfer Recipient
```py
from easypaystack.transfers import Transfer

paystack = Transfer(secret_key)
response = paystack.get_transfer_recipients(perPage=50, page=1)
```
### Get Single Transfer Recipient
```py
from easypaystack.transfers import Transfer

paystack = Transfer(secret_key)
response = paystack.get_single_transfer_recipient(recipient_code='')
```

### Update Transfer Recipient
```py
from easypaystack.transfers import Transfer

paystack = Transfer(secret_key)
response = paystack.update_transfer_recipient(recipient_code='', name="", email="", description="this param is optional")
```
### Update Transfer Recipient
```py
from easypaystack.transfers import Transfer

paystack = Transfer(secret_key)
response = paystack.delete_transfer_recipient(recipient_code='')
```

### Initiate Transfer

```py
response = paystack.initiate_transfer(recipient_code="", amount=9000, narration="")
```
Amount must be an instance of **int** or **float**, else a "TypeError" will be raised.

**Note**: Ensure you disable OTP from the Preferences tab on the Paystack Dashoard if you want your transfer to go instantly without the need to authorize it with an OTP.

### Verify a Transfer

```py
from easypaystack.verification import PaystackVerification

paystack = PaystackVerification(secret_key)
response = paystack.verify_transfer(reference)
```
### Get All Transfer
```py
from easypaystack.transfers import Transfer

paystack = Transfer(secret_key)
response = paystack.get_transfers(perPage=50, page=1)
```
### Check Account balance
```py
from easypaystack.transfers import Transfer

paystack = Transfer(secret_key)
response = paystack.get_balance()
```
### Resolve Card BIN(Bank Identification Number)
```py
from easypaystack.verification import PaystackVerification

paystack = PaystackVerification(secret_key)
response = paystack.resolve_card_bin(six_digit='first_six_digit')
```

### List All Banks
```py
from easypaystack.getters import Getters

paystack = Getters(secret_key)
response = paystack.get_banks(country="nigeria", currency="NGN")
```

####Remarks
Thank you for using easypaystack, if this package has helped you, you can give it a star⭐️ on github. Should you encounter any difficulty, you can open a github issue on this repo https://github.com/i-wizard/easypaystack.
