

#def causeError():
#    1/0

#def callcauseError():
#   causeError()

#callcauseError()


#try:
#   1/0
#   1 +'a'
#except ZeroDivisionError:
#    print(" zero division error accours")

#except TypeError:
#    print(" type error accours")

#except Exception as e:
#   print("some error come",type(e))


#print("hello")



def handleExceptions(func):
    def wrapper(*args):
        try:
            func(*args)
        except ZeroDivisionError as e:
            print(" zero division error accours",type(e))

        except TypeError as e:
            print(" type error accours", type(e))

        except Exception as e:
            print("some error come",type(e))
    return wrapper

@handleExceptions
def causeError(n):
    print(1+n)
causeError('a')
causeError(1)
causeError(2.0)

causeError(True)