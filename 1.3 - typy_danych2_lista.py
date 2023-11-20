# lista - kolekcja, przechowuje dowolną ilość, dowolnego typu danych

lista = []  # pusta lista
print(type(lista))

lista.append("Tomek")
lista.append("Radek")
lista.append("Zenek")
lista.append("Darek")
print(lista)  # ['Tomek', 'Radek', 'Zenek', 'Darek']
# lista zachowuje kolejnośc przy dodawaniu

# wypisac elemnt z listy po indeksie
print(lista[0])  # pierwsza pozycja
print(lista[-1])  # ostatnia pozycja
# ['Tomek', 'Radek', 'Zenek', 'Darek']
#    0(-4)     1(-3)    2(-2)  3(-1)
print(lista[0:3])  # ['Tomek', 'Radek', 'Zenek'] 0,1,2
print(lista[0], lista[3])  # Tomek Darek
print(lista[0:3:2])  # ['Tomek', 'Zenek'] :2 - krok

# zamiana na danym indeksi
lista[0] = "Kazik"
print(lista)  # ['Kazik', 'Radek', 'Zenek', 'Darek']

# insert() - wstawia(dodaje) pomiedzy dwa elemnty, indeks wskazuje w którym miejscu ma byc
lista.insert(1, "Grzegorz")
print(lista)  # ['Kazik', 'Grzegorz', 'Radek', 'Zenek', 'Darek']
print(len(lista))  # 5 długość listy

# usunięcie elemntu
lista.remove("Radek")
print(lista)  # ['Kazik', 'Grzegorz', 'Zenek', 'Darek']

lista.append("Kazik")
print(lista)  # ['Kazik', 'Grzegorz', 'Zenek', 'Darek', 'Kazik']
lista.remove("Kazik")
print(lista)  # ['Grzegorz', 'Zenek', 'Darek', 'Kazik']
# usunie pierwszego

print(lista.pop(3))  # Kazik
print(lista)  # ['Grzegorz', 'Zenek', 'Darek']
lista.pop(2)
print(lista)  # ['Grzegorz', 'Zenek']
print(lista.index("Zenek"))  # indeks 1
lista.append("Zenek")
print(lista)  # ['Grzegorz', 'Zenek', 'Zenek']
print(lista.index("Zenek"))  # 1 - dla pierwszego napotkanego

lista_copy = lista  # kopia referencji
lista_copy_ok = lista.copy()  # kopiowanie wszystkich elementów
print(lista)
print(lista_copy)
lista.clear()  # usuniecie wszystkich elemntów
print(lista_copy)  # []
print(id(lista))
print(id(lista_copy))
print(lista_copy_ok)
print(id(lista_copy_ok))  # 2698317231360
a = 7
b = 6
a = b
print(a)  # 6
b = 128
print(a)  # 6

liczby = [54, 999, 34, 22, 12.34, 876]
# liczby = [54, 999, 34, 22, 12.34, 876, 'Kazik']  # TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)
print(type(liczby))  # <class 'list'>
liczby.sort()  # sortowanie
print(liczby)  # [12.34, 22, 34, 54, 876, 999]
lista_lista = [1, 2, 3, [1, 2, 3]]
print(lista_lista)
print(type(lista_lista))  # <class 'list'>
# numpy - dedykowana do operacji na macierzach
