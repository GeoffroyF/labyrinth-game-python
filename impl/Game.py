import sys
from random import randint

from impl.Player import Player
from impl.game_saving.GameLoader import GameLoader
from impl.game_saving.GameSaver import GameSaver
from impl.labyrinth.Labyrinth import Labyrinth
from impl.command_manager.CommandManager import CommandManager


class Game:

    def __init__(self):
        print("Welcome to the Labyrinth Game")

    def initialize_game(self):
        """ Initialize the game by asking to choose to create a new game or to load a previous one."""
        game_init_method = ""
        while game_init_method != "load" and game_init_method != "new":
            game_init_method = input("Do you want to load or start a new game ? [load/new]: ")

        if game_init_method == "new":
            labyrinth_size = ""
            while (not labyrinth_size.isnumeric()) or int(labyrinth_size) < 4 or int(labyrinth_size) > 10:
                labyrinth_size = input("Please enter labyrinth size (4 to 10) :")
            labyrinth_size = int(labyrinth_size)

            self.__labyrinth = Labyrinth(labyrinth_size)
            player_pos_x, player_pos_y = self.__labyrinth.generate_labyrinth()
            self.__player = Player(int(player_pos_x), int(player_pos_y))

        else:
            success = False
            while success != True:
                self.__player = Player(0, 0)
                self.__labyrinth = Labyrinth(4)
                filename = input("Enter the filename (without the extension): ")
                try:
                    success = GameLoader().load_game([filename], self.__player, self.__labyrinth)
                    print("loaded successfully")
                except:
                    print("error while loading, verify the file name.")

    def start(self):
        """Starts the game loop"""
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
