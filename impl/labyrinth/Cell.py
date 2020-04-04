from .CellType import *


class Cell:
    def __init__(self, cell_type: CellType):
        self.__cell_type = cell_type

    def get_cell_type(self):
        return self.__cell_type

