
class Ljus():
    def __init__(self, driver, *args, **kwargs):
        self._driver = driver(*args, **kwargs)
