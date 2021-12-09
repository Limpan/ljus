from ljus.animation import Animation
from ljus.colors import WHITE


class Fill(Animation):
    def __init__(self, pixels, speed, color=WHITE):
        super().__init__(self, pixels, speed)
        self.color = color

    def draw(self):
        self._pixels.fill(self.color)
