from abc import ABCMeta, abstractmethod
from impl.labyrinth.Labyrinth import Labyrinth


class IPlayer(metaclass=ABCMeta):

    @abstractmethod
    def move_up(self, labyrinth: Labyrinth): pass

    @abstractmethod
    def move_down(self, labyrinth: Labyrinth): pass

    @abstractmethod
    def move_left(self, labyrinth: Labyrinth): pass

    @abstractmethod
    def move_right(self, labyrinth: Labyrinth): pass
