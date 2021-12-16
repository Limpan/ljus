import array
from rp2 import PIO, StateMachine, asm_pio
from ljus.pixels import Strip
import time


class DotStar(Strip):
    _sm = None
    _bitstream = None

    @asm_pio(sideset_init=PIO.OUT_HIGH, out_init=PIO.OUT_HIGH, out_shiftdir=PIO.SHIFT_LEFT)
    def _driver():
        pull()
        set(x, 31) [0]
        label("bitloop")
        out(pins, 1).side(0) [1]
        nop().side(1) [0]
        jmp(x_dec, "bitloop")

    def __init__(self, clock, data, n, brightness):
        super().__init__(n, brightness)

        self._cpin = clock
        self._dpin = data
        self._bitstream = array.array("I", [0] + [0] * self._n + [0xffff])
        self._sm = StateMachine(0, self._driver, freq=8000000, sideset_base=self._cpin, out_base=self._dpin)
        self._sm.active(1)
    
    def init(self):
        pass

    def _refresh(self):
        # Update self._bitstream
        for i in range(self._n):
            r, g, b, brightness = self._pixels[i]
            self._bitstream[i + 1] = int(brightness << 24 | b << 16 | g << 8 | r)

        # Start frame
        self._sm.put(0)

        self._sm.put(self._bitstream)

        # End frame
        self._sm.put(0xffff)


# https://github.com/raspberrypi/pico-micropython-examples/blob/master/pio/pio_uart_tx.py

# https://github.com/shreyask21/neopixel_rp2040/blob/main/neopixel_rp2040.py
# https://github.com/robert-hh/hx711/blob/master/hx711_pio.py
