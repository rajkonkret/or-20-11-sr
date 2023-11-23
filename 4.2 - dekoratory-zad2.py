def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper():
        result = func()  # wynik działania funkcji przekazanej
        return f"\033[1m" + result + "\033[0m"

    return wrapper  # zwracamy adres funkcji


@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello, World!"


print(greeting())
print("HELLO")