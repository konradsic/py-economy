class EconomyException(Exception):
    """
    Represents an economy exception.
    
    Used to handle most exceptions  in this project.

    Arguments
    -----------------
        message: :class:`str`
            An error/exception message
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        print(f"Economy function raised an error: {self.message}")

class InvalidParameter(EconomyException):
    """
    Inherits EconomyException
    
    Used when invalid parameter/s are passed to a function.

    Arguments
    -----------------
        message: :class:`str`
            An error/exception message
    """
    def __init__(self, message):
        super().__init__(message)

raise InvalidParameter("wow!")