from solver import Colour
from solvergui.asset import Asset


class Assets:

    colours = {
        Colour.ORANGE: Asset("solvergui/assets/orange.png"),
        Colour.BLUE: Asset("solvergui/assets/blue.png"),
        Colour.UNKNOWN: Asset("solvergui/assets/unknown.png"),
    }
