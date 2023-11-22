# stworzenie ksiązki telefonicznej z wykorzystaniem pętli while jako głównej pętli programu
# dodaj kontakt, usun kontakt, wyszukaj kontakt, wyswietl wszystkie kontakty
# wyjscie z programu

# wyswietlenie menu
# odczytanie od uzytkowynika wybranego elementu z menu
# w zaleznosci od wyboru wykonanie opercji
contacts = {}
while True:
    print(f"""
    1. Dodaj kontakt
    2. Usuń kontakt
    3. Wyszukaj kontakt
    4. Wyswietl wszystkie konatkty
    5. Koniec
""")
    odp = input('Wybierz opcję')

    try:
        if odp == '1':
            name = input("Podaj imie kontaktu")
            number = input("Podaj numer telefonu (tylko cyfry)")
            if not number.isdigit():
                raise ValueError("Numer telefonu powienien zawierac cyfry!")
            if name in contacts:
                print(f"Kontakt {name} już istnieje")
            else:
                contacts[name] = number
                print(f"Kontakt {name} został dodany")

        elif odp == '2':
            name = input("Podaj imię kontaktu do usunięcia")
            if name in contacts:
                del contacts[name]  # usuniecie el ze słownika
                # contacts.pop(name)  # usuniecie el ze słownika
                print(f"Kontakt {name} został usunięty.")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}.")

        elif odp == '3':
            pass
        elif odp == '4':
            if not contacts:
                print("Lista kontaktów jest pusta")
            for name, number in contacts.items():
                print(f"Kontakt {name} : {number}")
        else:
            break
    except KeyError:
        print(f"Nie znaleziono kontaktu o imieniu {name}.")
    except ValueError as ve:
        print(f"Bład wartości {ve}")
    except Exception as e:
        print("Wystąpił bład:", e)
    finally:  # zawsze
        print("Dziekuje za korzystanie z mojego programu")
