from ljus.animation import Animation
from ljus.colors import RAINBOW


class Fill(Animation):
    def __init__(self, pixels, speed, colors=RAINBOW):
        super().__init__(self, pixels, speed)
        self.colors = colors
        self.current_pos = 0

    def draw(self):
        self._pixels.fill(self.colors[self.current_pos])
        self.current_pos = (self.current_pos + 1) % len(self.colors)
