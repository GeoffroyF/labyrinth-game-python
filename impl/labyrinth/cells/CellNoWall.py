from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from services.ICell import ICell


class CellNoWall(Cell, ICell):
    """Cell that represent an empty space between other cells. The player can cross this cell while moving."""

    def __init__(self):
        super().__init__(CellType.NO_WALL)

    def __str__(self):
        return "-"

    def execute_action(self, labyrinth, player): pass
