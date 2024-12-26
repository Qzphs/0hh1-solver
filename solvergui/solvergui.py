import tkinter

from solver import Grid
from solvergui.tile_button import TileButton
from solvergui.ui import Ui


class SolverGui(Ui):

    def __init__(self):
        self.grid = Grid(12)
        self.main_window = tkinter.Tk()
        self.main_window.title("0hh1 solver by Qzphs")
        self.main_window.geometry(f"{600}x{480}")
        self._init_tile_frame()
        self._init_control_frame()
        self.display()

    def _init_tile_frame(self):
        self.tile_frame = tkinter.Frame(self.main_window)
        self.tile_frame.grid(row=0, column=0)
        self.tile_buttons = [
            TileButton(self.tile_frame, self, tile)
            for tile in self.grid.tiles()
        ]
        for tile_button in self.tile_buttons:
            tile_button.grid(row=tile_button.tile.u, column=tile_button.tile.v)

    def _init_control_frame(self):
        self.control_frame = tkinter.Frame(self.main_window)
        self.control_frame.grid(
            row=0, column=1, padx=(20, 0), sticky=tkinter.N
        )
        self.clear_button = tkinter.Button(
            self.control_frame, text="clear", command=self.clear
        )
        self.clear_button.grid(row=0, column=0)
        self.solve_button = tkinter.Button(
            self.control_frame, text="solve", command=self.solve
        )
        self.solve_button.grid(row=1, column=0)

    def display(self):
        for tile_button in self.tile_buttons:
            tile_button.display()

    def clear(self):
        self.grid.clear()
        self.display()

    def solve(self):
        self.grid.solve()
        self.display()

    def start(self):
        self.main_window.mainloop()
