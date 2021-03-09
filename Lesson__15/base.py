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
    def move(self, position):
        pass


p = Pawn('black', 'a2')
p.move('a3') # True
p.move('b3') # False
print(p.get_position())