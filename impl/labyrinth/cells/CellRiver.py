from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from impl.labyrinth.cells.CellEmpty import CellEmpty
from impl.objects.Treasure import Treasure
from services.ICell import ICell


class CellRiver(Cell, ICell):
    """Treasure Cell, when the player goes on this cell, he takes the treasure in his inventory"""

    def __init__(self, is_source):
        super().__init__(CellType.RIVER)
        self.is_source = is_source

    def __str__(self):
        return "R"

    def is_river_source(self):
        return self.is_source

    def execute_action(self, labyrinth,  player):
        """changes the player position"""

        p_x, p_y = player.get_pos()
        if self.is_river_source() == True:
            if labyrinth.get_labyrinth()[(p_y * 2 + 1)][p_x * 2 + 3].get_cell_type() == CellType.RIVER:
                print("player moved by the river")
                player.move_right(labyrinth)
            if labyrinth.get_labyrinth()[(p_y * 2 + 1)][p_x * 2 - 1].get_cell_type() == CellType.RIVER:
                player.move_left(labyrinth)