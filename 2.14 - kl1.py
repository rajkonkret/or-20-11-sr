# klasa - szablon
#  definicja klasa - tu sie nic nie wykona
import math


class MyFirstClass:
    """
    Kalsa w Pythonie, Reprezentuje punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        metoda inicjalizująca (tzw. konstruktor)
        :param x: x : int
        :param y: y : int
        """
        # self.x = x
        # self.y = y
        # dodalismy funkcje move(), która robi to samo, więc mozemy ją tutaj wykorzystać
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    # funkcja magiczna
    def __repr__(self):  # reprezentacja obiektu, co sie wyswieli jak uzyjemy print na obiekcie
        return f"x = {self.x}, y = {self.y}"


# print(MyFirstClass.__doc__)
#  Kalsa w Pythonie, Reprezentuje punkty w przestrzeni x i y
# wielolinijkowy komentarz jest traktowany jako dokumentacja
# print(print.__doc__)
ob = MyFirstClass()
# print(ob)  # <__main__.MyFirstClass object at 0x00000249A64B8090>
# po nadpisaniu __repr_ wyswiatla tak:
print(ob)  # x = 0, y = 0
print(ob.__str__())
ob2 = MyFirstClass(1, 5)
print(ob2)
ob2.move(10, 32)
print(ob2)
ob2.reset()
print(ob2)
ob.move(45, 76)
print(ob)
print(ob.calculate(ob2))  # 88.32326986700618

print("PI =", math.pi)  # PI = 3.141592653589793
print(math.sqrt(25))  # 5.0 float
