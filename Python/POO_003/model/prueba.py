class Punto:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
    
    def __str__(self):
        return f"Punto: ({self._x}, {self._y})"
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self, x: int):
        self._x = x
    @y.setter
    def y(self, y: int):
        self._y = y


if __name__ == "__main__":
    p = Punto(1, 2)
    p.x = 33
    print(p)