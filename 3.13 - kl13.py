class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą"))
    if x < 0:
        raise MyException('Liczba musi być dodatnia')
except MyException as e:
    print("Wystąpił wyjątek MyException", e)
except ValueError:
    print("Wystapił bład wartości")
except Exception as e:
    print("Bład", e)
