from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from impl.labyrinth.cells.CellEmpty import CellEmpty
from impl.objects.Treasure import Treasure
from services.ICell import ICell


class CellTreasure(Cell, ICell):

    def __init__(self):
        super().__init__(CellType.TREASURE)

    def __str__(self):
        return "T"

    def execute_action(self, labyrinth,  player):
        player.add_object(Treasure())
        p_x, p_y = player.get_pos()
        labyrinth.set_cell(p_x * 2 + 1, p_y * 2 + 1, CellEmpty())
