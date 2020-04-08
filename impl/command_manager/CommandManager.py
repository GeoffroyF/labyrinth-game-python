from impl.command_manager.commands import *
from services.commands import IUserCommand


class CommandManager:

    def __init__(self):
        self.__supported_commands = CommandManager.make_commands_dict(
            [Quit(),
             GoDown(),
             GoUp(),
             GoLeft(),
             GoRight(),
             Skip(),
             ShowLabyrinth(),
             GoUpShort(),
             GoRightShort(),
             GoLeftShort(),
             GoDownShort(),
             SaveGame(),
             LoadGame()
             ])

    def parse_user_input(self, user_input):
        tokens = user_input.strip().split(" ")

        if len(tokens) == 0:
            return None, None, ""

        norm_cmd = tokens[0].lower()

        if norm_cmd in self.__supported_commands:
            cmd = self.__supported_commands[norm_cmd]
            return cmd, tokens[1:10], ""

        return None, None, "Command not supported: "

    @staticmethod
    def eval_command(cmd: IUserCommand, args, labyrinth, player):
        if cmd.get_args_count() != len(args):
            return (False, "Invalid number of args. Expected: "
                    + str(cmd.get_args_count()) + ", " + "got: " + str(len(args)))
        return cmd.evaluate(args, labyrinth, player)

    @staticmethod
    def make_commands_dict(cmd_lst):
        cmd_dict = dict()
        for cmd in cmd_lst:
            cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
        return cmd_dict
