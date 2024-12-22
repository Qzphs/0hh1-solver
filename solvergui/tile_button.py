import tkinter

from solver import Grid, Tile
from solvergui.assets import Assets
from solvergui.ui import Ui


class TileButton(tkinter.Button):

    def __init__(self, master, grid: Grid, ui: Ui, tile: Tile):
        super().__init__(master, command=self.click)
        self._grid = grid
        self.ui = ui
        self.tile = tile
        self.display()

    def click(self):
        self.tile.colour = self.tile.colour.next()
        self.ui.display()

    def display(self):
        self.config(image=Assets.colours[self.tile.colour].image())
