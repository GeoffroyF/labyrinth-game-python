import sys
from random import randint

from impl.Player import Player
from impl.labyrinth.Labyrinth import Labyrinth
from impl.command_manager.CommandManager import CommandManager


class Game:

    def __init__(self):
        print("Welcome to the Labyrinth Game")

    def initialize_game(self):
        labyrinth_size = int(input("Please enter labyrinth size :"))
        player_pos_x = randint(0, labyrinth_size-1)
        player_pos_y = randint(0, labyrinth_size-1)

        self.__labyrinth = Labyrinth(labyrinth_size)
        self.__labyrinth.generate_labyrinth(player_pos_x, player_pos_y)
        self.__player = Player(player_pos_x, player_pos_y)

    def start(self):
        command_manager = CommandManager()
        finished = False
        message = ""
        state = ""
        args = []
        cmd = None
        try:
            while not finished:
                user_input = input("$> ")

                cmd, args, message = command_manager.parse_user_input(user_input)
                if cmd == None:
                    print(message)
                    continue
                (finished, state, message) = CommandManager.eval_command(cmd, args, state, self.__labyrinth, self.__player)
                print(str(state))
                if message != "": print(message)
        except:
            print("Unexpected error:", sys.exc_info()[0])
