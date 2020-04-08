from impl.objects.Object import LabyrinthObject
from impl.objects.Treasure import Treasure
from services.IPlayer import IPlayer
from impl.labyrinth.Labyrinth import Labyrinth
from impl.labyrinth.CellType import CellType


class Player(IPlayer):

    def __init__(self, pos_x: int, pos_y: int):
        self.__objects = []
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def add_object(self, obj: LabyrinthObject):
        """adds object to the object list"""
        self.__objects.append(obj)

    def remove_object(self, obj: LabyrinthObject):
        """Remove object from the object list"""
        self.__objects.pop(self.__objects.index(obj))

    def get_objects(self):
        return self.__objects

    def set_objects(self, objects):
        self.__objects = objects

    def get_current_cell(self, labyrinth: Labyrinth):
        """Return the cell on which the player is"""
        return labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][self.__pos_x * 2 + 1]

    def get_pos(self):
        return self.__pos_x, self.__pos_y

    def set_pos(self, x, y):
        self.__pos_x = x
        self.__pos_y = y

    def execute_cell_action(self, labyrinth: Labyrinth):
        """Execute the action of the cell on which the player is"""
        current_cell = self.get_current_cell(labyrinth)
        current_cell.execute_action(labyrinth, self)

    def move_up(self, labyrinth: Labyrinth):
        """Make the player move up if there are no wall or monolith. If the player has the treasure and moves out
        it triggers the win action"""
        above_cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1) - 1][self.__pos_x * 2 + 1].get_cell_type()
        if above_cell == CellType.WALL or above_cell == CellType.MONOLITH:
            return "step impossible", above_cell.value, False
        elif above_cell == CellType.NO_WALL and self.__pos_y == 0 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif above_cell == CellType.NO_WALL and self.__pos_y == 0 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_y -= 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def move_down(self, labyrinth: Labyrinth):
        """Make the player move odwn if there are no wall or monolith. If the player has the treasure and moves out
                it triggers the win action"""
        underneath__cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1) + 1][self.__pos_x * 2 + 1].get_cell_type()
        if underneath__cell == CellType.WALL or underneath__cell == CellType.MONOLITH:
            return "step impossible", underneath__cell.value, False
        elif underneath__cell == CellType.NO_WALL and self.__pos_y == labyrinth.get_size() - 1 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif underneath__cell == CellType.NO_WALL and self.__pos_y == labyrinth.get_size() - 1 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_y += 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def move_left(self, labyrinth: Labyrinth):
        """Make the player move left if there are no wall or monolith. If the player has the treasure and moves out
                it triggers the win action"""
        left_cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][(self.__pos_x * 2 + 1) - 1].get_cell_type()
        if left_cell == CellType.WALL or left_cell == CellType.MONOLITH:
            return "step impossible", left_cell.value, False
        elif left_cell == CellType.NO_WALL and self.__pos_x == 0 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif left_cell == CellType.NO_WALL and self.__pos_x == 0 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_x -= 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def move_right(self, labyrinth: Labyrinth):
        """Make the player move right if there are no wall or monolith. If the player has the treasure and moves out
                it triggers the win action"""
        right_cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][(self.__pos_x * 2 + 1) + 1].get_cell_type()
        if right_cell == CellType.WALL or right_cell == CellType.MONOLITH:
            return "step impossible", right_cell.value, False
        elif right_cell == CellType.NO_WALL and self.__pos_x == labyrinth.get_size() - 1 and self.player_has_treasure():
            return "step executed", "out of labyrinth", True
        elif right_cell == CellType.NO_WALL and self.__pos_x == labyrinth.get_size() - 1 and not self.player_has_treasure():
            return "step impossible", "no treasure in inventory", False
        else:
            self.__pos_x += 1
            return "step executed", self.get_current_cell(labyrinth).get_cell_type().value, False

    def player_has_treasure(self):
        """Checks if the player has the treasure in his inventory """
        return True in [isinstance(obj, Treasure) for obj in self.__objects]
