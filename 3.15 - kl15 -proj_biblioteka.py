#  stworzyc system zarzadzania biblioteką, któy umożliwa dodawanie ksiązek, wypozyczanie oraz zwracanie ksiązek
# nalezy pamiętac jakie ksiazki posiadamyw  bibliotece a jakie wypozyczone
# klasy Book, Library
# __repr_
# obsłuzyc błedy
# rozszerzenie user co wypożyczył ksiązce

class Book:
    # autor, tytuł, isbn
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    # __repr__
    def __repr__(self):
        return f"Autor: {self.author}, Tytuł: {self.title}, ISBN: {self.isbn}"


class Library:
    # lista ksiazek dostepnych
    # lista ksiazek wypożyczonych

    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    # metody:
    # dodaj_ksiazke
    # wypozycz_ksiazke
    # zroc_ksiazke
    # dostepne_ksiazki
    # wypozyczone_ksiazki
    # wyszukaj_ksiazke
    def dodaj_ksiazke(self, book):
        self.dostepne_ksiazki.append(book)

    def dostepne_ksiazki_fun(self):
        return self.dostepne_ksiazki

    def wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.remove(book)
                self.wypozyczone_ksiazki.append(book)
                return book
        return Exception("Nie mam takiej ksiązki")

    def zwroc_ksiazki(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.remove(book)
                self.dostepne_ksiazki.append(book)
                return True
        return Exception("Ksiązka nie z naszej biblioteki")

    def wypozyczone_ksiazki_fun(self):
        return self.wypozyczone_ksiazki

    def wszystkie_ksiazki(self):
        return self.wypozyczone_ksiazki + self.dostepne_ksiazki

    def znajdz_ksiazke(self, isbn):
        # for book in self.dostepne_ksiazki:
        #     if book.isbn == isbn:
        #         return "dostepne ksiązki", book
        # for book in self.wypozyczone_ksiazki:
        #     if book.isbn == isbn:
        #         return "wypożyczone ksiązki", book
        dk, book = self.przeszukaj_liste(self.dostepne_ksiazki, isbn)
        wk, book = self.przeszukaj_liste(self.wypozyczone_ksiazki, isbn)
        if dk:
            return book, "dostepne ksiazki"
        elif wk:
            return book, "wypozyczone ksiązki"
        else:
            raise Exception("Brak książki")

    def przeszukaj_liste(self, lista, isbn):
        for book in lista:
            if book.isbn == isbn:
                return True, book
        return False


biblioteka = Library()
biblioteka.dodaj_ksiazke(Book("programowanie w Pythonie", "Jan Kowalski", "1234567890"))
biblioteka.dodaj_ksiazke(Book("programowanie w Pythonie cz2", "Jan Kowalski", "1234567891"))
print(f"Wszystkie ksiązki {biblioteka.wszystkie_ksiazki()}")
print(f"Dostępne ksiązki {biblioteka.dostepne_ksiazki_fun()}")
# Wszystkie
# ksiązki[Autor: Jan
# Kowalski, Tytuł: programowanie
# w
# Pythonie, ISBN: 1234567890, Autor: Jan
# Kowalski, Tytuł: programowanie
# w
# Pythonie
# cz2, ISBN: 1234567891]
# Dostępne
# ksiązki[Autor: Jan
# Kowalski, Tytuł: programowanie
# w
# Pythonie, ISBN: 1234567890, Autor: Jan
# Kowalski, Tytuł: programowanie
# w
# Pythonie
# cz2, ISBN: 1234567891]
print(f"Wypożyczone ksiązki {biblioteka.wypozyczone_ksiazki_fun()}")
# Wypożyczone ksiązki []
wypozyczona = biblioteka.wypozycz_ksiazke("1234567890")
print(f"Wypożyczona ksiązka {wypozyczona}")
# Wypożyczona ksiązka Autor: Jan Kowalski, Tytuł: programowanie w Pythonie, ISBN: 1234567890
print(f"Wypożyczone ksiązki {biblioteka.wypozyczone_ksiazki_fun()}")
print(f"Dostępne ksiązki {biblioteka.dostepne_ksiazki_fun()}")
