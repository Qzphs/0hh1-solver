from solver.colour import Colour


class Candidate:

    def __init__(self, seed: int, size: int):
        self.colours: list[Colour] = []
        for _ in range(size):
            self.colours.append(Colour(seed % 2))
            seed >>= 1

    def valid(self):
        n_orange = self.colours.count(Colour.ORANGE)
        n_blue = self.colours.count(Colour.BLUE)
        if n_orange != n_blue:
            return False
        for i in range(len(self.colours) - 2):
            if self.colours[i] == self.colours[i + 1] == self.colours[i + 2]:
                return False
        return True
