

def handleExpection(fun):
    def wrapper(*args):
        try:
            fun(*args)
        except TypeError:
            print("type error")
        
        except ZeroDivisionError:
            print("zero division error")
        
        except Exception as e:
            print("something is error", type(e))
    
    return wrapper


@handleExpection
def function():
    print("im in function")

@handleExpection
def causError(n):
    1+n
    1/n

function()
causError(1)
causError(0)



print("helo")