# match case

lang = input("Podaj znany Ci język")  # pobiera np.: od użytkownika z klawiatury
# input zwraca str

match lang.lower().replace(" ", ""):
    case "java":
        print("Lubię jave")
    case "python":
        print("Miał byc prosty")
    case "c++":
        print("kto to jeszcze używa?")
    case _:
        print("Działanie domyślne")


