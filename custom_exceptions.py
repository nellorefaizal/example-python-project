
class CustomException(Exception):
    pass
def causeError():
    raise CustomException("this is a custom Expection")

#causeError()

class HttpException(Exception):
    satuscode= None
    message=None

    def __int__(self):
        super().__init__(f'statuscode: {self.satuscode} an d message{self.message}')

class NotFound(HttpException):
    satuscode=404
    message="resourse not found"

class ServerError(HttpException):
    satuscode=500
    message="the server is having trouble"

def raiseServerError():

    raise ServerError()

raiseServerError()
