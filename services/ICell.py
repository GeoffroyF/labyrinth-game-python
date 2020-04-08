from abc import ABCMeta, abstractmethod


class ICell(metaclass=ABCMeta):
    """INterface for all cells"""

    @abstractmethod
    def __str__(self) -> str: pass

    @abstractmethod
    def execute_action(self, labyrinth, player): pass
