# while - petla sterowana warunkiem

licznik = 0

while True:
    licznik += 1 # licznik = licznik + 1
    print("Komunikat")
    if licznik > 10:
        break

print(licznik) #11
licznik = 0
while licznik < 10:
    print("Komunikat 2")
    licznik += 1

lista = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(int(wej))

print(lista)  # [4, 5, 6]


