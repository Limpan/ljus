from ljus.animation import Animation
from ljus.colors import WHITE


class Pulse(Animation):
    def __init__(self, pixels, speed, color=WHITE):
        super().__init__(pixels, speed)
        self.color = color
        self.alpha = 255
        self.beta = 0.5
        self.gamma = 0.2

    def draw(self):


        self._pixels.fill([self.current_intensity] * 3)
        self.current_intensity = (self.current_intensity + 1) % 256
