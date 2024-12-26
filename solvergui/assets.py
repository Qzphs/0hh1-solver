from solver import Colour
from solvergui.asset import Asset


class Assets:

    colours = [
        Asset("solvergui/assets/orange.png"),
        Asset("solvergui/assets/blue.png"),
        Asset("solvergui/assets/unknown.png"),
    ]

    @classmethod
    def colour(cls, colour: Colour):
        return cls.colours[colour.index]
