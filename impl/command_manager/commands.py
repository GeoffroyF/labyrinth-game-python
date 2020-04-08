from impl.game_saving.GameLoader import GameLoader
from impl.game_saving.GameSaver import GameSaver
from services.commands import IUserCommand


class Quit(IUserCommand):
    """ Quit command to stop the game"""
    def get_command_tag(self):
        return "quit"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        return True, "Finished"


class GoUp(IUserCommand):
    """Triggers move up action"""
    def get_command_tag(self):
        return "go-up"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_up(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoDown(IUserCommand):
    """Triggers move down action"""
    def get_command_tag(self):
        return "go-down"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_down(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoLeft(IUserCommand):
    """Triggers move left action"""
    def get_command_tag(self):
        return "go-left"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_left(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class GoRight(IUserCommand):
    """Triggers move right action"""
    def get_command_tag(self):
        return "go-right"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        success, above_cell, won = player.move_right(labyrinth)
        player.execute_cell_action(labyrinth)
        return won, str(success) + ": " + str(above_cell)


class Skip(IUserCommand):
    """Skip the player turn and trigger the current cell action"""
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        player.execute_cell_action(labyrinth)
        return False, "step executed"


class GoUpShort(GoUp):
    def get_command_tag(self):
        return "z"


class GoDownShort(GoDown):
    def get_command_tag(self):
        return "s"


class GoLeftShort(GoLeft):
    def get_command_tag(self):
        return "q"


class GoRightShort(GoRight):
    def get_command_tag(self):
        return "d"


class ShowLabyrinth(IUserCommand):
    """prints the labyrinth in the console"""
    def get_command_tag(self):
        return "show"

    def get_args_count(self):
        return 0

    def evaluate(self, args, labyrinth, player):
        labyrinth.show_labyrinth()
        return False, "labyrinth shown"


class SaveGame(IUserCommand):
    """Saves the game to the given filename"""
    def get_command_tag(self):
        return "save"

    def get_args_count(self):
        return 1

    def evaluate(self, args, labyrinth, player):
        saver = GameSaver()
        try:
            saver.save_game(args, player, labyrinth)
        except:
            return False, "error while saving"
        return False, "Game saved successfully"


class LoadGame(IUserCommand):
    """load game from the given filename"""
    def get_command_tag(self):
        return "load"

    def get_args_count(self):
        return 1

    def evaluate(self, args, labyrinth, player):
        loader = GameLoader()
        try:
            loader.load_game(args, player, labyrinth)
        except:
            return False, "error while loading"
        return False, "Game loaded successfully"
