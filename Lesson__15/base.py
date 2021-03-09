from abc import ABC, abstractmethod


class BaseFigure(ABC):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        print("Draw figure on position:", self.color)

    @abstractmethod
    def move(self, x, y):
        pass

    def get_position_x(self):
        return self.x

    def get_position_y(self):
        return self.y


class Pawn(BaseFigure):
    def move(self, x, y):
        """
        1 - x должен быть тот же
        2 - y должен повышаться на 1 или на 2 в первый ход
        3 - поменять позиции на новые
        """
        if x != self.x:
            return False

        elif self.y == 2:
            if y - self.y > 2 or y == self.y:
                return False
        elif y - self.y > 1:
            return False
        self.y = y
        self.x = x
        return True


class Elephant(BaseFigure):
    def move(self, x, y):
        if self.x == x:
            return False

        if abs(self.x - x) == abs(self.y - y):
            self.y = y
            self.x = x
            return True

        return False


class Human(ABC):
    @abstractmethod
    def greet(self):
        pass


class Kyrgyz(Human):
    def greet(self):
        print("Саламалекум")


class Russian(Human):
    def greet(self):
        print("Привет")

k = Kyrgyz()
k.greet()
r = Russian()
r.greet()