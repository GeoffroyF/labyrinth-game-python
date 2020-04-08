from impl.labyrinth.CellType import CellType


class Cell:
    """Mother class of cells, each class will have get_cell_type """

    def __init__(self, cell_type: CellType):
        self.__cell_type = cell_type

    def get_cell_type(self):
        return self.__cell_type
