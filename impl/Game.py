import sys
from random import randint

from impl.Player import Player
from impl.labyrinth.Labyrinth import Labyrinth
from impl.command_manager.CommandManager import CommandManager


class Game:

    def __init__(self):
        print("Welcome to the Labyrinth Game")

    def initialize_game(self):
        labyrinth_size = ""
        while (not labyrinth_size.isnumeric()) or int(labyrinth_size) < 4 or int(labyrinth_size) > 10:
            labyrinth_size = input("Please enter labyrinth size (4 to 10) :")
        labyrinth_size = int(labyrinth_size)

        self.__labyrinth = Labyrinth(labyrinth_size)
        player_pos_x, player_pos_y = self.__labyrinth.generate_labyrinth()
        self.__player = Player(int(player_pos_x), int(player_pos_y))

    def start(self):
        command_manager = CommandManager()
        finished = False
        message = ""
        args = []
        cmd = None
        try:
            while not finished:
                user_input = input("$> ")

                cmd, args, message = command_manager.parse_user_input(user_input)
                if cmd == None:
                    print(message)
                    continue
                (finished, message) = CommandManager.eval_command(cmd, args, self.__labyrinth, self.__player)
                if message != "": print(message)
            print("End of Game !")
        except:
            print("Unexpected error:", sys.exc_info()[0])
