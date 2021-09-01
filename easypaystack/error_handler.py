class MyErrors(Exception):
    '''Base Class Error'''
    pass

class InputError(MyErrors):
    '''Error raised when there is a missing input field'''
    pass

class ValueError(MyErrors):
    '''Error raised when the wrong value  is used'''
    pass

class TypeError(MyErrors):
    '''Error raised when the wrong data type is used'''
    pass

class AuthKeyError(MyErrors):
    '''Error raised when the user doesn\'t add a secret key'''
    pass

class RequestMethodError(MyErrors):
    '''Error is raised when an invalid request method is passed'''
    pass