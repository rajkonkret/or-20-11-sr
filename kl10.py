import pickle
from dataclasses import dataclass


# klasa Person

# class Person:
#     def __init__(self, first_name, last_name, id):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.id = id

@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greets(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to {self.id} ")


# Sprawdza czy wywołany bezpośrednio
# jesli tak wykona ten kod
# jesli wywołąny z innego pliku ten kod sie nie wywoła
if __name__ == '__main__':
    p2 = Person("Maciek", "Nowak", 1)
    print(p2)  # Person(first_name='Maciek', last_name='Nowak', id=1)
    p1 = Person("Jacek", "Kowalski", "1")
    print(p1)

    people = [
        Person("Jacek", "Kowalski", 1),
        Person("Mateusz", "Zegar", 2)
    ]
    print(people)
    # [Person(first_name='Jacek', last_name='Kowalski', id=1),
    #  Person(first_name='Mateusz', last_name='Zegar', id=2)]

    with open('dane.pickle', "wb") as stream:  # filehandler
        pickle.dump(people, stream)  # zapisujemy liste people klas Person do pliku ze zmiennej stream
