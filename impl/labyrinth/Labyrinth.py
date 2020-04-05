from random import randint

from impl.labyrinth.cells.CellEmpty import CellEmpty
from impl.labyrinth.cells.CellMonolith import CellMonolith
from impl.labyrinth.cells.CellNoWall import CellNoWall
from impl.labyrinth.cells.CellStart import CellStart
from impl.labyrinth.cells.CellTreasure import CellTreasure
from impl.labyrinth.cells.CellWall import CellWall


class Labyrinth:

    def __init__(self, size: int):
        self.__size = size
        self.__labyrinth = []

    def get_labyrinth(self):
        return self.__labyrinth

    def get_size(self):
        return self.__size

    def generate_random_treasure_pos(self, player_x, player_y):
        treasure_x = -1
        treasure_y = -1
        while (treasure_x < 0 or treasure_y < 0) or (treasure_x == player_x and treasure_y == player_y):
            treasure_x = randint(0, self.__size - 1)
            treasure_y = randint(0, self.__size - 1)
        return treasure_x, treasure_y

    def generate_random_exit(self):
        exit_x = randint(1, self.__size * 2 - 1)
        exit_y = randint(1, self.__size * 2 - 1)
        if randint(0, 1) == 0:
            exit_x = randint(0, 1) * (self.__size * 2)
        else:
            exit_y = randint(0, 1) * (self.__size * 2)
        return exit_x, exit_y

    def generate_labyrinth(self, player_x: int, player_y: int):
        treasure_x, treasure_y = self.generate_random_treasure_pos(player_x, player_y)
        exit_x, exit_y = self.generate_random_exit()
        print(exit_x, exit_y)
        grid_size = self.__size * 2 + 1
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                if exit_x == j and exit_y == i:
                    row.append(CellNoWall())
                elif i == 0 or i == grid_size - 1 or j == 0 or j == grid_size - 1:  # monolith
                    row.append(CellMonolith())

                elif i % 2 == 0 or j % 2 == 0:
                    if randint(1, 10) < 4:
                        row.append(CellWall())
                    else:
                        row.append(CellNoWall())

                elif (player_x * 2 + 1) == j and (player_y * 2 + 1) == i:
                    row.append(CellStart())

                elif (treasure_x * 2 + 1) == j and (treasure_y * 2 + 1) == i:
                    row.append(CellTreasure())

                else:
                    row.append(CellEmpty())

            self.__labyrinth.append(row)

    def show_labyrinth(self):
        for i in self.__labyrinth:
            for j in i:
                print(j, end="")
            print("")

    def set_cell(self, pos_x: int, pos_y: int, cell):
        self.__labyrinth[pos_y][pos_x] = cell
