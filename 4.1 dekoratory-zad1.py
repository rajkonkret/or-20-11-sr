# dekoratory - @staticmethod
# funkcja opakowująca inną funkcje w dodatkowe własciwosci
# zbudowaane są na zasadzie funkcji wewnętrznej
def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # zwroci wynik dziłanai funkcji przekazanej

    return wew


@dekor
def hej():
    print("Hej!!!")


hej()  # uruchomienie funkcji
# Po dodaniu dekoratora
# Dekorujemy
# Hej!!!
