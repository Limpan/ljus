
class Strip():
    def __init__(self, n, brightness = 1.0):
        self._n = n
        self.brightness = brightness
        self._pixels = [(0xff, 0, 0, 0)] * self._n


    def _color(self, *value):
        if not len(value) == 3:
            raise ValueError("Got tuple of length {} when expecting 3.".format(len(value)))

        br = 0b11100000 | (int(self.brightness * 31) & 0b00011111)
        r, g, b = value

        return r, g, b, br


    def fill(self, color):
        r, g, b = color
        self._pixels[::] = [self._color(r, g, b)] * len(self)


    def __len__(self):
        return self._n


    def __setitem__(self, index, value):
        if isinstance(index, slice):
            start, stop, step = index.indices(self._n)
            for value_i, index_i in enumerate(range(start, stop, step)):
                r, g, b = value[value_i]
                self._pixels[index_i] = self._color(r, g, b)
        else:
            r, g, b = value
            self._pixels[index] = self._color(r, g, b)


    def __getitem__(self, index):
        if isinstance(index, slice):
            out = []
            for index_i in range(*slice.indices(self._n)):
                out.append(self._pixels[index_i])
            return out

        if index < 0:
            index += len(self)
        if index >= self._n or index < 0:
            raise IndexError
        return self._pixels[index]


    def _refresh(self):
        raise NotImplementedError("Must be implemented in subclass.")
    