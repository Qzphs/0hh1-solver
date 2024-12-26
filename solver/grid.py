import itertools

from solver.colour import Colour
from solver.strip import Strip
from solver.tile import Tile


class Grid:

    def __init__(self, size: int):
        self.size = size
        self._tiles = [[Tile(u, v) for v in range(size)] for u in range(size)]
        self.rows = [Strip(row) for row in self._tiles]
        self.columns = [
            Strip([row[i] for row in self._tiles]) for i in range(size)
        ]

    def tile(self, u: int, v: int):
        """Return the tile at (u, v)."""
        return self._tiles[u][v]

    def tiles(self):
        """Return a (non-nested) list of all tiles."""
        return sum(self._tiles, start=[])

    def unknown(self):
        """
        Returns an arbitrary unknown tile.

        If the grid is complete, return None instead.
        """
        for tile in self.tiles():
            if tile.colour != Colour.UNKNOWN:
                continue
            return tile
        return None

    def unknowns(self):
        """Return a list of all unknown tiles."""
        return [tile for tile in self.tiles() if tile.colour == Colour.UNKNOWN]

    def clear(self):
        """Mark all tiles as unknown."""
        for row in self._tiles:
            for tile in row:
                tile.colour = Colour.UNKNOWN

    def solve(self):
        """Fill in unknown tiles."""
        search_frontier = [self]
        while search_frontier:
            this = search_frontier.pop()
            this.deduce()
            if this.invalid():
                continue
            if not this.unknowns():
                self.replace(this)
                return
            search_frontier.extend(self.split())

    def deduce(self):
        """Fill in unknown tiles using basic deductions."""
        previous_unknowns = 999
        while previous_unknowns > len(self.unknowns()):
            previous_unknowns = len(self.unknowns())
            for row in self.rows:
                row.deduce()
            for column in self.columns:
                column.deduce()

    def invalid(self):
        """Return True if there are no more solutions for this grid."""
        if any(strip.invalid() for strip in self.rows + self.columns):
            return True
        for row1, row2 in itertools.combinations(self.rows, 2):
            if Colour.UNKNOWN in row1.colours():
                continue
            if Colour.UNKNOWN in row2.colours():
                continue
            if row1.colours() == row2.colours():
                return True
        for column1, column2 in itertools.combinations(self.columns, 2):
            if Colour.UNKNOWN in column1.colours():
                continue
            if Colour.UNKNOWN in column2.colours():
                continue
            if column1.colours() == column2.colours():
                return True
        return False

    def replace(self, other: "Grid"):
        """Replace tile colours with `other`'s tile colours."""
        if self.size != other.size:
            raise ValueError
        for tile in self.tiles():
            tile.colour = other.tile(tile.u, tile.v).colour

    def split(self):
        """
        Return two copies of this grid.

        Choose an arbitrary unknown in this grid. Fill in that tile with
        a colour on one of the copies, and the opposite colour on the
        other copy.
        """
        copy1 = Grid(self.size)
        copy1.replace(self)
        copy2 = Grid(self.size)
        copy2.replace(self)
        unknown = self.unknown()
        copy1.tile(unknown.u, unknown.v).colour = Colour.ORANGE
        copy2.tile(unknown.u, unknown.v).colour = Colour.BLUE
        return copy1, copy2
