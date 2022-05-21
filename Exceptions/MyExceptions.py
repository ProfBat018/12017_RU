class ArgumentTypeError(BaseException):
    def __init__(self, message, code=1):
        self.message = message
        self.code = code


class OutOfRangeError(BaseException):
    def __init__(self, message, code=1):
        self.message = message
        self.code = code

