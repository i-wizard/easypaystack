from easypaystack.error_handler import *


def amount_validator(amount=None):
    if amount is None:
        raise InputError('Amount must be a number')
    if not isinstance(amount, int) or not isinstance(amount, float):
        raise TypeError('Amount must be a valid number')
    if amount <= 0:
        raise InputError('Amount must be greater than zero')
    return amount
