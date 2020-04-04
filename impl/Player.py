from impl.objects.Object import LabyrinthObject
from services.IPlayer import IPlayer
from impl.labyrinth.Labyrinth import Labyrinth
from impl.labyrinth.CellType import CellType


class Player(IPlayer):

    def __init__(self, pos_x, pos_y):
        self.__objects = []
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def add_object(self, obj: LabyrinthObject):
        self.__objects.append(obj)

    def remove_object(self, obj: LabyrinthObject):
        self.__objects.pop(self.__objects.index(obj))

    def move_up(self, labyrinth: Labyrinth):
        above_cell = labyrinth.get_labyrinth()[(self.__pos_y*2+1) - 1][self.__pos_x*2+1].get_cell_type()
        if above_cell == CellType.WALL or above_cell == CellType.MONOLITH:
            return "step impossible", above_cell.value
        else:
            self.__pos_y -= 1
            return "step executed", labyrinth.get_labyrinth()[(self.__pos_y*2+1)][self.__pos_x*2+1].get_cell_type().value

    def move_down(self, labyrinth: Labyrinth):
        underneath__cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1) + 1][self.__pos_x * 2 + 1].get_cell_type()
        if underneath__cell == CellType.WALL or underneath__cell == CellType.MONOLITH:
            return "step impossible", underneath__cell.value
        else:
            self.__pos_y += 1
            return "step executed", labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][self.__pos_x * 2 + 1].get_cell_type().value

    def move_left(self, labyrinth: Labyrinth):
        left_cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][(self.__pos_x * 2 + 1) - 1].get_cell_type()
        if left_cell == CellType.WALL or left_cell == CellType.MONOLITH:
            return "step impossible", left_cell.value
        else:
            self.__pos_x -= 1
            return "step executed", labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][
                self.__pos_x * 2 + 1].get_cell_type().value

    def move_right(self, labyrinth: Labyrinth):
        right_cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][(self.__pos_x * 2 + 1) + 1].get_cell_type()

        if right_cell == CellType.WALL or right_cell == CellType.MONOLITH:
            return "step impossible", right_cell.value
        else:
            self.__pos_x += 1
            return "step executed", labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][
                self.__pos_x * 2 + 1].get_cell_type().value
