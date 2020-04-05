from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from services.ICell import ICell


class CellStart(Cell, ICell):

    def __init__(self):
        super().__init__(CellType.STARTING_CELL)

    def __str__(self):
        return "S"

    def execute_action(self, labyrinth, player): pass
