# set  (zbior) - przechowuje unikalne elementy
# nie zachowuje kolejnosci przy dodawaniu elemntów

lista = [44, 55, 66, 77, 33, 11, 55, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 11, 44, 77, 55}
zbior.add(18)
zbior.add(18)
zbior.add(33)
print(zbior)  # {33, 66, 11, 44, 77, 18, 55}
print(sorted(zbior))  # [11, 18, 33, 44, 55, 66, 77]
# sorted() - posortowana lista z elementami zbioru

# usunie pierwszy element ze zbioru
print(zbior.pop())  # 33
print(zbior.pop())  # 66
print(zbior.pop())  # 11
print(zbior.pop())  # 44
print(zbior)  # {77, 18, 55}

# usunięcie po elemencie
zbior.remove(18)
print(zbior)  # {77, 55}

zbior_liczb = {66, 11, 44, 18, 55, 62, 999, 999}
print(zbior_liczb)  # {66, 18, 55, 999, 11, 44, 62}

zb2 = set()  # pusty zbior
print(zb2)  # set() tak wyswietli pusty set

print(zbior | zbior_liczb)  # suma zbiorów {66, 999, 11, 44, 77, 18, 55, 62}
print(zbior & zbior_liczb)  # częśc wspólna {55}
print(zbior - zbior_liczb)  # {77}
print(zbior.difference(zbior_liczb))  # {77}
# union nnie modyfikuje bazowej kolekcji
zbior.union(zbior_liczb)  # zbior i zbior_liczb nie zostają zmienione
print(zbior)
print(zbior_liczb)
print(zbior)  # {77, 55}
print(zbior.union(zbior_liczb))  # {66, 999, 11, 44, 77, 18, 55, 62}
zbior_zmod = zbior.union(zbior_liczb)
print(f"Zbior zmodyfikowany: {zbior_zmod}")
# Zbior zmodyfikowany: {66, 999, 11, 44, 77, 18, 55, 62}
# update()) modyfikuje kolekcje
zbior.update(zbior_liczb)  # zbior zostaje zmienione
print(zbior)  # {66, 999, 11, 77, 44, 18, 55, 62}
# 10: 40