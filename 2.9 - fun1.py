# funkcje - fragment kodu, który możemy wykonac wielokrotnie w dowolnym momencie
# funkcja musi byc najpierw zdefiniowana, dopiero po zdefiniowaniu możemy jej użyc
a = 6
b = 7


# definicja funkcji
def dodaj():
    # pass  # nic nie rób
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):  # c=0 domyslna wartośc argumentu
    print(a - b - c)


def mnozenie(a, b):
    return a * b


def mnozenie2(a, b):
    return a, b, a * b


# wykonanie funkcji
dodaj()  # 13
dodaj2(6, 9)  # 15
odejmij(1, 2, 3)
odejmij(1, 2)
print(odejmij(1, 2, 3))  # None
print(mnozenie(5, 6))
print(mnozenie(5, 6) + mnozenie(9, 10))
print(mnozenie2(3, 4))  # (3, 4, 12)
a, b, c = mnozenie2(5, 6)
print(f"Wynik {a} * {b} = {c}")
# Wynik 5 * 6 = 30
odejmij(c=9, b=8, a=5)  # -12 można podac argumenty po nazwie
