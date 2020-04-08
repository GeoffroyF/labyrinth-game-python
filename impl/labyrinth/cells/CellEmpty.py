from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from services.ICell import ICell


class CellEmpty(Cell, ICell):
    """Empty cell where the player can walk"""

    def __init__(self):
        super().__init__(CellType.EMPTY)

    def __str__(self):
        return "*"

    def execute_action(self, labyrinth, player): pass

