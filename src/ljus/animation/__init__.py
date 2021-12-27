import time

TICKS_PER_S = 1000

class Animation():
    def __init__(self, pixels, speed):
        self._pixels = pixels
        self._speed = speed
        self._step_next_update = int(TICKS_PER_S / self._speed)
        self._next_update = time.ticks_ms()
        self.draw_count = 0
    

    def animate(self):
        now = time.ticks_ms()

        if now > self._next_update:
            self.draw_count += 1
            self.draw()
            self.show()

            self._next_update += self._step_next_update


    def draw(self):
        raise NotImplementedError()


    def show(self):
        self._pixels._refresh()


from .fill import Fill
from .cycle import Cycle
from .rainbow import Rainbow
from .pulse import Pulse