# krotka - kolekcja niezmienna
# indexowanie od 0

tupla = ("Radek",)  # jednoelementowa tupla
print(type(tupla))  # <class 'tuple'>
temp2 = 36, 6  # <class 'tuple'>
print(type(temp2))
tupla2 = "Tomek", "Radek", "Zenek", "Magda"
print(tupla2)  # ('Tomek', 'Radek', 'Zenek', 'Magda')
print(type(tupla2))  # <class 'tuple'>

print(tupla2.index("Radek"))  # 1
print(tupla2.count("Tomek"))  # 1

tupla3 = 44, 34, 22.43, 11, 200
print(type(tupla3))  # <class 'tuple'>

print(tupla2[0])  # Tomek
# tupla2[0] = "Maciek"  # TypeError: 'tuple' object does not support item assignment

# rozpakowanie tupli
a, b = 1, 2
print(a)  # 1
print(b)  # 2

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3
print(a)  # 1
print(b)  # [2, 3]

# ('Tomek', 'Radek', 'Zenek', 'Magda')
# imie1, imie2, imie3 = tupla2

*imie1, imie2, imie3 = tupla2
print(imie1, imie2, imie3)  # ['Tomek', 'Radek'] Zenek Magda

imie1, *imie2, imie3 = tupla2
print(imie1, imie2, imie3)  # Tomek ['Radek', 'Zenek'] Magda

imie1, imie2, *imie3 = tupla2
print(imie1, imie2, imie3)  # Tomek Radek ['Zenek', 'Magda']
# * - worek na pozostałe elementy
print(imie1, imie2)  # Tomek Radek

lista_krotka = list(tupla2)  # rzutowanie tuple na liste
print(type(lista_krotka))  # <class 'list'>
print(lista_krotka)  # ['Tomek', 'Radek', 'Zenek', 'Magda']
