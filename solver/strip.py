from solver.candidate import Candidate
from solver.candidates import candidates
from solver.colour import Colour
from solver.tile import Tile


class Strip:

    def __init__(self, tiles: list[Tile]):
        self.tiles = tiles

    def size(self):
        return len(self.tiles)

    def colours(self):
        return [tile.colour for tile in self.tiles]

    def invalid(self):
        """Return True if there are no more solutions for this strip."""
        colours = self.colours()
        if colours.count(Colour.ORANGE) > self.size() // 2:
            return True
        if colours.count(Colour.BLUE) > self.size() // 2:
            return True
        for i in range(self.size() - 2):
            if colours[i] == colours[i + 1] == colours[i + 2] == Colour.ORANGE:
                return True
            if colours[i] == colours[i + 1] == colours[i + 2] == Colour.BLUE:
                return True
        return False

    def deduce(self):
        """Fill in unknown tiles using basic deductions."""
        remaining = [
            candidate
            for candidate in candidates(self.size())
            if self._consistent(candidate)
        ]
        if not remaining:
            return
        for i in range(self.size()):
            if self.tiles[i].colour != Colour.UNKNOWN:
                continue
            if any(
                candidate.colours[i] != remaining[0].colours[i]
                for candidate in remaining
            ):
                continue
            self.tiles[i].colour = remaining[0].colours[i]

    def _consistent(self, candidate: Candidate):
        for tile_colour, candidate_colour in zip(
            self.colours(), candidate.colours
        ):
            if tile_colour == Colour.UNKNOWN:
                continue
            if tile_colour == candidate_colour:
                continue
            return False
        return True
