from abc import ABCMeta, abstractmethod
from impl.labyrinth.Labyrinth import Labyrinth


class IPlayer(metaclass=ABCMeta):
    """interface for the player class"""
    @abstractmethod
    def move_up(self, labyrinth: Labyrinth): pass

    @abstractmethod
    def move_down(self, labyrinth: Labyrinth): pass

    @abstractmethod
    def move_left(self, labyrinth: Labyrinth): pass

    @abstractmethod
    def move_right(self, labyrinth: Labyrinth): pass
