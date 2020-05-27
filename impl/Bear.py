from impl.Player import Player
from random import randint

from impl.labyrinth.cells.CellBear import CellBear


class Bear(Player):
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y)
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def move_random(self, labyrinth):
        moving_option = randint(0, 3)
        prev_x = self.__pos_x
        prev_y = self.__pos_y

        has_moved = False
        if moving_option == 0:
            executed, cell, finished = self.move_left(labyrinth)
            if executed == "step executed":
                self.__pos_x -= 1
                has_moved = True
        if moving_option == 1:
            executed, cell, finished = self.move_right(labyrinth)
            if executed == "step executed":
                self.__pos_x += 1
                has_moved = True
        if moving_option == 2:
            executed, cell, finished = self.move_up(labyrinth)
            if executed == "step executed":
                self.__pos_y -= 1
                has_moved = True
        if moving_option == 3:
            executed, cell, finished = self.move_down(labyrinth)
            if executed == "step executed":
                self.__pos_y += 1
                has_moved = True
        if has_moved:
            self.__prev_cell = labyrinth.get_labyrinth()[(self.__pos_y * 2 + 1)][(self.__pos_x * 2 + 1)]
            print(self.__prev_cell)
            print(prev_x, prev_y, self.__pos_x, self.__pos_y)
            labyrinth.set_cell(self.__pos_x * 2 + 1, self.__pos_y * 2 + 1, CellBear())
            labyrinth.set_cell(prev_x * 2 + 1, prev_y * 2 + 1, self.__prev_cell)



