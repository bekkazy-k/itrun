class Car:
    def __init__(self, name):
        self.name = name
        self._speed = 0

    def up_speed(self):
        self._speed += 10
        print('Speed:', self._speed)

    def down_speed(self):
        self._speed += 10
        print('Speed:', self._speed)

    def get_speed(self):
        return self._speed


c = Car("Audi")
c.up_speed()
c.up_speed()
c.up_speed()
# print(c.get_speed())
print(c.get_speed())