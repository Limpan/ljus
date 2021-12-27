# micropython-ljus

Package that aims to simplify lighting and animation of LEDs. Primarily for RP2040 and APA102 LEDs.

# Development

## Connecting to MCU
Connecting with rshell is simple.
```
rshell -p /dev/ttyACM0 --buffer-size 512
```

To syncronize code `rsync . /rp2040/lib` can be used when in the `src` folder.


## Upload to PyPI

First create source distribution package.
```
python3 setup.py sdist
```

Then upload to PyPI.
```
twine upload dist/*.tar.gz
```
