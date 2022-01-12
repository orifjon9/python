# Exception- raise
x = -1
# if x < 0:
#     raise Exception("A value should be possitive")

# assert
# assert((x < 0), "Must be possitive")

# try except
try:
    b = x / 0
except ZeroDivisionError:
    print("Zero division")
except TypeError:
    print("Type error")
except Exception as e:
    print(e)
else:
    print("Something else was happen")
finally:
    print("cleaning up...")


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message: str, value: int) -> None:
        self.message = message
        self.value = value


def check_value(x: int):
    if x > 100:
        raise ValueTooHighError("A Value is larger than 100")
    if x < 5:
        raise ValueTooSmallError("A value is small", x)


try:
    check_value(200)
    # check_value(4)
    # check_value("one")
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as ex:
    print(ex.message, ex.value)
except TypeError:
    print("An argument got a wrong type")
