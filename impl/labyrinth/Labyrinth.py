from .Cell import *
from random import randint


class Labyrinth:

    def __init__(self, size: int):
        self.__size = size
        self.__labyrinth = []

    def generate_labyrinth(self, player_x, player_y):
        treasure_x = -1
        treasure_y = -1
        while (treasure_x < 0 or treasure_y < 0) or (treasure_x == player_x and treasure_y == player_y):
            treasure_x = randint(0, self.__size - 1)
            treasure_y = randint(0, self.__size - 1)

        grid_size = self.__size * 2 + 1
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                if i == 0 or i == grid_size-1 or j == 0 or j == grid_size-1: # monolith
                    if randint(1, 10) > 2:
                        row.append(Cell(CellType.MONOLITH))
                    else:
                        row.append(Cell(CellType.NO_WALL))

                elif i%2 == 0 or j%2 == 0:
                    if randint(1, 10) > 2:
                        row.append(Cell(CellType.WALL))
                    else:
                        row.append(Cell(CellType.NO_WALL))

                elif (player_x*2+1) == j and (player_y*2+1) == i:
                    row.append(Cell(CellType.STARTING_CELL))

                elif (treasure_x*2+1) == j and (treasure_y*2+1) == i:
                    row.append(Cell(CellType.TREASURE))

                else:
                    row.append(Cell(CellType.EMPTY))

            self.__labyrinth.append(row)

    def show_labyrinth(self):
        for i in self.__labyrinth:
            for j in i:
                if j.get_cell_type() == CellType.MONOLITH:
                    print("M", end="")
                if j.get_cell_type() == CellType.EMPTY:
                    print("*", end="")
                if j.get_cell_type() == CellType.STARTING_CELL:
                    print("S", end="")
                if j.get_cell_type() == CellType.WALL:
                    print("W", end="")
                if j.get_cell_type() == CellType.NO_WALL:
                    print("-", end="")
                if j.get_cell_type() == CellType.TREASURE:
                    print("T", end="")

            print("")




