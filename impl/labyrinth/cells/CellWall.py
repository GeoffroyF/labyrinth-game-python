from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from services.ICell import ICell


class CellWall(Cell, ICell):
    """ Cell class that represent a wall that th player cannot cross while moving"""

    def __init__(self):
        super().__init__(CellType.WALL)

    def __str__(self):
        return "W"

    def execute_action(self, labyrinth, player): pass
