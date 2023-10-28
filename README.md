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

**NOTE** whenever you import any class from the easypaystack sdk, always instantiate it with your secret key else it will raise a "MissinAuthKeyError"
*Remember to never include your **secret key** ❌ in your code, instead use environment variables like the example below*.
```py
from decouple import config

secret_key = config("PAYSTACK_SECRET")
paystack = PaystackVerification(secret_key)
```

## PAYMENTS
### Initiate Payment
Initiate a payment. This method initiates a pending transaction on paystack.
Its is advisable to also create a pending transaction using this generated reference because you'll need it to verify this transaction after it's completed on the brower.
```py
from easypaystack.payment import Payment

paystack = Payment(secret_key)
response = paystack.initiate_payment(email="david@gmail.com", kobo_amount=5000, reference="uniquers453")
```
### Verify Payment
Verify a payment. Use the reference generated during the transaction
initiation to verify this payment
```py
from easypaystack.verification import PaystackVerification

paystack = PaystackVerification(secret_key)
response = paystack.verify_payment(reference=payment_reference)
```

### Charge Authorization
This method is used in recurring payments like subscriptions or
monthly repayment.
The user's card must have been tokenized prior to using this method call.
You only tokenize a card once. 
To tokenize a card you need to use it for at least one payment transaction with minimum amount of about 100 naira then save the authorization code gotten from the payment verification response.
Charge Authorization is a one step process, this means once you call this method the user is automatically debited, you don't need the user's input to perform this.
The email address used here must be the same address used during the card tokenization
```py
from easypaystack.payment import Payment

paystack = Payment(secret_key)
response = paystack.charge_authorization(authorization_code="authorization_code", email="david@gmail.com", kobo_amount=5000, reference="uniquers453")
```

## TRANSFERS
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

## UTILS
#### Resolve Account Number
```py
from easypaystack.verification import PaystackVerification
```
```py
paystack = PaystackVerification(secret_key)
response = paystack.resolve_account(account_number, bank_code)
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
