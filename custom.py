
class CustomException(Exception):
    pass

def causeError():
    raise CustomException('This is a custom exception')


# causeError()

class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(f'status code: {self.statusCode} and message is {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = "Resource not found"

class ServerError(HttpException):
    statusCode = 500
    message = "The server is having some trouble"

def raiseServerError():
    raise ServerError()

raiseServerError()