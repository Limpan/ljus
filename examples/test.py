from machine import Pin
from ljus import colors
from ljus.drivers.dotstar_rp2 import DotStar
import time

cpin = Pin(15)
dpin = Pin(25)

d = DotStar(cpin, dpin, 6, 0.5)
d.fill(colors.RED)
d._refresh()
