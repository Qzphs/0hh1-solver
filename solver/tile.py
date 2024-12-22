from solver.colour import Colour


class Tile:

    def __init__(self, u: int, v: int):
        self.u = u
        self.v = v
        self.colour = Colour.UNKNOWN
