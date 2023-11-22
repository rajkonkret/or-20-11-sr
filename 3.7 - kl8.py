from abc import ABC, abstractmethod


# bo dodaniu metody abstrakcyjnej ta klasa jest abstrakcyjna
# nie można utworzyc obiektu(instancji) tej klasy
# trzeba nadpisac w klasach dziedziczących metody abstrakcyjne
class Counter(ABC):

    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    # oznaczenie metody jako abstrakcyjnej
    @abstractmethod
    def drukuj(self):
        pass

    # metoda statyczna, nie trzeba tworzyc obiektu klasy
    # by jej uzyc
    @staticmethod
    def format_string(x):
        return "format string %d"

    @classmethod
    def from_counter(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartość nie może być przekroczyć MAX")
        super().__init__(values)

    # musimy nadpisac metode abstrakcyjną
    def drukuj(self):
        print("Drukuje...", self.values)


# c = Counter()
# c.increment()
# print(c)
# c.drukuj()  # pass
# c.increment(10)
# print(c)
# c.drukuj()
bc = BoundedCounter(10)
bc.drukuj()  # Drukuje... 10
print(Counter.format_string(5))  # format string %d
d = BoundedCounter.from_counter(bc)
d.drukuj()  # Drukuje... 10
e = BoundedCounter(bc.values)  # cls(counter.values)
# 12:35
