from impl.objects.Object import LabyrinthObject
from services.IPlayer import IPlayer
from impl.labyrinth.Labyrinth import Labyrinth


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
        # {if actual cell does not hava a wall && another wall on top
        # then move

        print("up")

    def move_down(self, labyrinth: Labyrinth):
        print("down")

    def move_left(self, labyrinth: Labyrinth):
        print("left")

    def move_right(self, labyrinth: Labyrinth):
        print("right")
