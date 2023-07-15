class Color:

    def __init__(self, color: str) -> None:
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color: str):
        self._color = color

    def __str__(self):
        return f'Datos Color = Color: { self._color }'