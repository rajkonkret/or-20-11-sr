# kalkulator z petla while, przechwycic wyjatki
# ksiazka telefoniczna doadaj numer, wyswietl wszystkie, dane pojedynczego, usun
# wyjscie z programu

# wyswielnie opcji
# pobranie opcji
# pobranie liczb
# wykonanie obliczenia
# wyswietlenie wyniku lub błedu

lista = [1, 2, 3, 4, 5]
print(5 in lista)  # True

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Jakie działąnie chcesz wykonać?")  # str
    # if odp == "5":
    #     break
    # if odp > "5":
    #     break
    if odp not in ["1", "2", "3", "4"]:  # lista zdeklarowana w miejsu uzycia
        break

    try:
        while True:
            try:
                a = float(input("Podaj liczbę a"))
                break
            except ValueError:
                print("To nie jest poprawna liczba")

        while True:
            try:
                b = float(input("Podaj liczbę b"))
                break
            except ValueError:
                print("To nie jest poprawna liczba")
        # 12:45
        if odp == "1":
            print(f"Wynik działania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik działania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik działania {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik działania {a} / {b} = {a / b}")
    except  ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Błąd", e)
