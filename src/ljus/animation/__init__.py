import time

class Animation():
    def __init__(self, pixels, speed):
        self._pixels = pixels
        self._speed = speed
        self._next_update = time.ticks_ms()
        self.draw_count = 0
    
    def animate(self):
        now = time.ticks_ms()

        if now < self._next_update:
            self.draw_count += 1
            self.draw()
            self.show()

    def draw(self):
        raise NotImplementedError()
    
    def show(self):
        self._pixels.show()
    