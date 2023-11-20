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
print(wiek ** rok)  # potęgowanie
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
print("Zmienna flat {}".format(5.755555))  # Zmienna flat 5.755555

wersja = 3.9000001
print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.9000001
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
# dla 0f zaokrąglił przy wypisywaniu
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4
print(wersja)  # 3.9000001
wersja2 = 3.999999
print(f"Uzywamy wersji python {wersja2:.3f}")  # # Uzywamy wersji python 4.000
wersja3 = 3.9994567
print(f"Uzywamy wersji python {wersja3:.3f}")  # # Uzywamy wersji python 3.999
wersja4 = 3.9995567
print(f"Uzywamy wersji python {wersja4:.3f}")  # Uzywamy wersji python 4.000

print(f"""
tekst wielolinijkowy
    zmienna {temp}
zmienna {wiek}""")
# "tekst wielolinijkowy
#     zmienna 36.6
# zmienna 47"
print(f"\tZmienna {temp}\nzmienna {wiek}")
# "	Zmienna 36.6
# zmienna 47"
# \t tabulator
# \n nowa linia
# \b - backspace
print("Jak działą backspce\b")  # Jak działą backspc

imie = "Radek Radek"
print(type(imie))
imie.lower()  # """ Return a copy of the string converted to lowercase. """
# zwraca kopię ale nie zmienia orginału
print(imie)
# gdy chcemy wyswietlic zmienione musimy
print(imie.lower())  # radek radek
print(imie)  # Radek Radek
# gdy potrzeebujemy w dalszej częsci zmienione to musimy zapamietac sobie
imie2 = imie.lower()
print(imie2)  # radek radek
print(imie)  # Radek Radek
# teksty w pythonie są niemutowalne
# tekst to jest tak naprawdę ciąg znaków
# kązda literka ma swój indeks(numer w ciągu)
print(imie[0])  # R - dla indeksu 0 - numeracja indeksów od 0
# imie[0] = "T"  # TypeError: 'str' object does not support item assignment
print(id(imie))  # 2000569352752 - referencja, adres w pamieci
# upper, cpitalize
imie_x = "Radek"
print(id(imie_x))
imie_x = imie_x.lower()
print(id(imie_x))
# 2041495767984
# 2041497701360
print(imie_x.replace("k", ","))  # rade,
print(imie_x.count("a"))  # 1
print(imie.capitalize())  # Radek radek - pierwsza litera duża, pozostałe małe
print(imie.title())  # Radek Radek - wszystkie wyrazy z duzej litery

liczba = 456789123456
print(liczba)  # 456789123456
print(f"Nasza duża liczba {liczba}")  # Nasza duża liczba 456789123456
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,789,123,456
# zamienic , na . i spacje
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))
# Nasza duża liczba 456 789 123 456
# Nasza duża liczba 456.789.123.456
liczba2 = 1111123.4565
print(f"Nasza duża liczba {liczba2:,}")  # Nasza duża liczba 1,111,123.4565
# 15:10

# boolean - typ logiczny
# True, False - z dużej litery, podobnie jak None
czy_znasz_Python = True
print(czy_znasz_Python)  # True
print(int(czy_znasz_Python))  # 1
print(int(False))  # 0
# bool() - zamiana na bool
print(bool(1))  # True
print(bool(0))  # False
print(bool(100))  # True
print(bool(-1))  # True
print(bool("Radek"))  # True
x = "Radek"
print(bool(x))  #
x = ""
print(bool(x))  # False
print(bool(None))  # False
# None - nic, odpowiednik nulla
z = None
print("z =", z)  # z = None
print(type(z))  # <class 'NoneType'>
# komentarz
"""
Komentarz wielolinijkowy
"""
tekst = "  Tekst   "
print(tekst.strip())  # "Tekst"
tekst_x = "Witaj świecie"
encoded_s = tekst_x.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'  b - zapis bytowy
print(type(encoded_s))  # <class 'bytes'>
# \x - dane w sytemie 16, \xc5  = 197
print(encoded_s.decode('utf-8'))  # Witaj świecie
tekst_kazik = "Zażółć gęślą jaźń"
encoded_kazik_s = tekst_kazik.encode('utf-8')
print(encoded_kazik_s)  # b'Za\xc5\xbc\xc3\xb3\xc5\x82\xc4\x87 g\xc4\x99\xc5\x9bl\xc4\x85 ja\xc5\xba\xc5\x84'
print(encoded_kazik_s.decode('utf-8'))
print(chr(65))  # A  - wyswietlenia z naku wg kodu ascii
print(ord('A'))  # 65
print("\u0105")  # ą
print("\uc487")  # 쒇
