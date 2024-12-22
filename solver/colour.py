from enum import Enum


class Colour(Enum):

    ORANGE = 0
    BLUE = 1
    UNKNOWN = 2

    def next(self):
        return Colour((self.value + 1) % len(Colour))
