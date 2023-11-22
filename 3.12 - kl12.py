class Boat:
    """
    Dokumntacja klasy
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # pole jest prywatne

    def sail(self):
        self.__speed += 20

    def speedometer(self):
        print("Speed in knots", self.__speed)


b1 = Boat("Omega", 2023)
b1.sail()
b1.sail()
b1.sail()
b1.sail()
# print(b1.__speed)  # 80, po ustawieniu pola jako prywatne AttributeError: 'Boat' object has no attribute '__speed'
b1.speedometer()  # Speed in knots 80
b1.__speed = 0  # pole globalne obiektu przypadkowo o tej samej nazwie co pole prywatne
b1.speedometer()  # Speed in knots 80
print(b1.__speed)  # 0
