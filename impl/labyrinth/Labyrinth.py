from random import randint

from impl.labyrinth.CellType import CellType
from impl.labyrinth.cells.CellEmpty import CellEmpty
from impl.labyrinth.cells.CellMonolith import CellMonolith
from impl.labyrinth.cells.CellNoWall import CellNoWall
from impl.labyrinth.cells.CellStart import CellStart
from impl.labyrinth.cells.CellTreasure import CellTreasure
from impl.labyrinth.cells.CellWall import CellWall
from impl.labyrinth.cells.CellWormhole import CellWormhole


class Labyrinth:
    """Labyrinth Class, it features the generation and the management of cells"""

    def __init__(self, size: int):
        self.__size = size
        self.__labyrinth = []

    def get_labyrinth(self):
        return self.__labyrinth

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def set_labyrinth(self, labyrinth):
        self.__labyrinth = labyrinth

    def generate_random_exit(self):
        """ Generate a random location for the exit"""
        exit_x = randint(1, self.__size) * 2 - 1
        exit_y = randint(1, self.__size) * 2 - 1
        if randint(0, 1) == 0:
            exit_x = randint(0, 1) * (self.__size * 2)
        else:
            exit_y = randint(0, 1) * (self.__size * 2)
        return exit_x, exit_y

    def initialize_special_cells(self):
        """All cells that have an action and a specific location are prepared here and returned in an array"""
        nb_wormholes = 0
        if self.__size < 7:
            nb_wormholes = 3
        elif self.__size < 9:
            nb_wormholes = 4
        else:
            nb_wormholes = 5
        special_cells = [CellWormhole(i+1, nb_wormholes) for i in range(nb_wormholes)]
        special_cells += [CellTreasure(), CellStart()]
        return special_cells

    def generate_walls(self, exit_x, exit_y, grid_size, row, i, j):
        """It generates the monolith, the exit and the walls. A classic wall has a 40% chance to pop randomly"""
        if exit_x == j and exit_y == i:
            row.append(CellNoWall())
        elif i == 0 or i == grid_size - 1 or j == 0 or j == grid_size - 1:  # monolith
            row.append(CellMonolith())
        elif i % 2 == 0 or j % 2 == 0:
            if randint(1, 10) < 4:
                row.append(CellWall())
            else:
                row.append(CellNoWall())
        else:
            return False
        return True

    def generate_labyrinth(self):
        """Main generation function that either trigger the geenrate walls , put an empy cell or put a special cell"""
        special_cells = self.initialize_special_cells()

        exit_x, exit_y = self.generate_random_exit()
        start_x, start_y = -1, -1
        grid_size = self.__size * 2 + 1
        number_of_active_cells = self.__size * self.__size
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                is_wall_space = self.generate_walls(exit_x, exit_y, grid_size, row, i, j)
                if not is_wall_space:
                    if randint(0,100) < int((float(len(special_cells)) / number_of_active_cells)*100):
                        index = randint(0, len(special_cells)-1)
                        row.append(special_cells[index])
                        if special_cells[index].get_cell_type() == CellType.STARTING_CELL:
                            start_x = (j - 1) / 2
                            start_y = (i - 1) / 2
                        special_cells.pop(index)
                    else:
                        row.append(CellEmpty())
                    number_of_active_cells -= 1

            self.__labyrinth.append(row)
        return start_x, start_y

    def show_labyrinth(self):
        """print each cells of the labyrinth"""
        for i in self.__labyrinth:
            for j in i:
                print(j, end="")
            print("")

    def export_labyrinth(self):
        """:returns a string with the labyinth represented by symbols"""
        export = ""
        for i in self.__labyrinth:
            for j in i:
                export += str(j)
            export += "\n"
        return export

    def set_cell(self, pos_x: int, pos_y: int, cell):
        """Sets a cell at a specific location"""
        self.__labyrinth[pos_y][pos_x] = cell
