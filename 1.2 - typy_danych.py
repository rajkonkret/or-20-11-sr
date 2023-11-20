print("Radek")  # wypisz/wydrukj - wyswietla tekst

print(type("Radek"))  # type() sprawdzenie typu danych, <class 'str'>
# ctrl alt l - formatuje kod wg zasad PEP8
print("93")
print(type("93"))  # <class 'str'>
# typowanie dynamiczne
# zmienna - pudełko na dane
wiek = 39
print(type(39))  # <class 'int'> liczba całkowita
wiek = "Radek"
print(type(wiek))  # <class 'str'>
wiek: str = "Radek"  # :str to jest tylko podpowiedz dla nas (hint), nie weryfikuje typy
print(wiek)
wiek = 39
print(type(wiek))  # <class 'int'>
print(wiek)  # 39
print("14" + "23")  # 1423 - konkatenacja, złaczanie stringów
# print(14 + "23")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(int("14") + int("23"))  # 37 int() - rzutowanie, zamiana na typ int(całkowite)
# print(int("") + int("29"))  # ValueError: invalid literal for int() with base 10: ''
# ctrl / - szybkie zakomentowania
print(5 * "RADEK")  # RADEKRADEKRADEKRADEKRADEK mnozenie stringów
print(160 * "25")

wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - zmiennoprzecinkowe, znak oddzielajacy kropka
print(type(temp))  # <class 'float'>
temp2 = 36, 6
print(type(temp2))  # <class 'tuple'> - to nie jest liczba

print(0.1 + 0.5)  # 0.6
# ctrl d - kopiowanie lini
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# zapamiętywane w postaci wykłądniczej n * 2 ^ x
# z tego wynika bład zaokrąglenia
# decimal - do liczenia pieniedzy, wolniejszy

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023232822540781017 float
print(1 / 1)  # 1.0
# 2070
# -1976
# 95081
# 0.023232822540781017
print(wiek // rok)  # 0, czesc całkowita z dzielenia 47/2023 = 0 całych i 47 reszty
print(wiek % rok)  # 47, modulo, reszta z dzielenia 47/2023 = 0 całych i 47 reszty

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0
print("Radek")
print('Radek')
# Radek
# Radek

print(wiek, rok)  # 47 2023
# sep
#         string inserted between values, default a space.
print(wiek, rok, sep=";")  # 47;2023
# end
#         string appended after the last value, default a newline.
print(wiek, rok, end='')  # ustawienie znaku nowej lini jako pusty ''
print("Nowa linia w starej linii")  # 47 2023Nowa linia w starej linii, tutaj juz domyslnie end="\n"
print("Nowa linia")
# 47;2023
# 47 2023Nowa linia w starej linii
# Nowa linia
# starszy sposób wypisywania
imie = "Radek"
print("Twoje imie %s" % imie)  # Twoje imie Radek
# ten sposób sprawdza typ
print("Twoje imie %s" % 39.7)
# print("Twoja liczba %d" % imie)  # TypeError: %d format: a real number is required, not str
# %d liczba całkowita
# %s string

print("Twoje imie {}".format(imie))  # Twoje imie Radek
print("Sprawdzam zmienna temp i wiek {} {}".format(wiek, temp))  # Sprawdzam zmienna temp i wiek 47 36.6
print(f"Sprawdzam zmienną temp {temp} i wiek {wiek}")  # Sprawdzam zmienną temp 36.6 i wiek 47
# f-string - sformatowany string
print("Zmienna flat {}".format(5.755555)) # Zmienna flat 5.755555
