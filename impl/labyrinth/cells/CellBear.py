from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from services.ICell import ICell


class CellBear(Cell, ICell):
    """Empty cell where the player can walk"""

    def __init__(self):
        super().__init__(CellType.BEAR)

    def __str__(self):
        return "B"

    def execute_action(self, labyrinth, player): pass

