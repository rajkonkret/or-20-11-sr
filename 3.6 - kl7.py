# wielodziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(A, B):
    """
    klasa C dziedziczy po A i B
    """

    # wypisze swoje, wypisze z bezposredniego dziedziczenia (A),
    # z B
    def method(self):
        print("Metoda z klasy C")
        super().method()  # dziedziczy z A
        B.method(self)


class D(B, A):
    """
    kalsa D
    """

    def method(self):
        print("Metoda klasy D")
        # ja chce w klasie uzyc dodatkowo zachowanie tej metody z klasy B
        super().method()  # super() w tym przypadku klasa B
        # i dodatkowo działanie z klasy A
        A.method(self)


a = A()
a.method()

b = B()
b.method()
# Metoda z klasy A
# Metoda z klasy B
c = C()
c.method()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
d = D()
d.method()
print(D.__mro__)
# Metoda z klasy B
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
