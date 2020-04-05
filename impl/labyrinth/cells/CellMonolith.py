from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from services.ICell import ICell


class CellMonolith(Cell, ICell):

    def __init__(self):
        super().__init__(CellType.MONOLITH)

    def __str__(self):
        return "M"

    def execute_action(self, labyrinth, player): pass
