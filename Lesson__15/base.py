from abc import ABC, abstractmethod


class BaseFigure(ABC):
    def __init__(self, color, position):
        self.color = color
        self._position = position

    def draw(self):
        print("Draw figure on position:", self.color)
    
    @abstractmethod
    def move(self, position):
        pass

    def get_position(self):
        return self._position


print("♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟ ♠")