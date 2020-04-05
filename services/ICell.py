from abc import ABCMeta, abstractmethod


class ICell(metaclass=ABCMeta):

    @abstractmethod
    def __str__(self) -> str: pass

    @abstractmethod
    def execute_action(self, labyrinth, player): pass
