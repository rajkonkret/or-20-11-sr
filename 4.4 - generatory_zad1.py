def kwadrat(n):
    for x in range(n):  # 0..n-1, petla zawsze startuje od 0
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # petla zpamietuje gdzie skonczyła, zapamietuje wartos x po kolejnym wywołaniu


kwa = kwadrat2(5)
print(next(kwa))  # 0 next() - kolejne wywołanie generatora
print(next(kwa))  # 1
print("Zrob cokolwiek")
print("wypisz cokolwiek")
lista = []
lista.append("1234567890")
print(lista)
print(next(kwa))  # 4
# 10:10
print(type(kwa))  # <class 'generator'>
print(next(kwa))
print(next(kwa))
# print(next(kwa))  # StopIteration  - wyczerpany generator. zakończył działanie
kwa2 = kwadrat2(6)
print("kwa2", next(kwa2))
print("kwa2", next(kwa2))
kwa3 = kwadrat2(5)
print("kwa3", next(kwa3))
