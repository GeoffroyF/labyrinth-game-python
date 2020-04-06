from impl.labyrinth.Cell import Cell
from impl.labyrinth.CellType import CellType
from services.ICell import ICell


class CellWormhole(Cell, ICell):

    def __init__(self, hole_number: int, total_holes: int):
        super().__init__(CellType.WORMHOLE)
        self.__number = hole_number
        self.__total_holes = total_holes

    def __str__(self):
        return str(self.__number)

    def get_number(self):
        return self.__number

    def execute_action(self, labyrinth, player):
        full_size = labyrinth.get_size() * 2 + 1
        for y in range(full_size):
            for x in range(full_size):
                if labyrinth.get_labyrinth()[y][x].get_cell_type() == CellType.WORMHOLE:
                    if labyrinth.get_labyrinth()[y][x].get_number() % self.__total_holes == (self.__number + 1) % self.__total_holes:
                        player.set_pos(int((x-1)/2), int((y - 1) / 2))
        print("*pow* -> Teleported to WormHole number " + str((self.__number + 1) % self.__total_holes))

