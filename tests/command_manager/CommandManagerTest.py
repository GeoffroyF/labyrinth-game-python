import unittest

from impl.Player import Player
from impl.command_manager.CommandManager import CommandManager, Quit, GoDown, GoUp, GoLeft, GoRight, Skip
from impl.labyrinth.Labyrinth import Labyrinth


class CommandManagerTest(unittest.TestCase):

    def test_parse_user_input(self):
        command_manager = CommandManager()
        commands = ["quit", "go-down", "go-up", "go-left", "go-right", "skip", "show", "save", "load"]
        for i in range(len(commands)):
            cmd, tokens, message = command_manager.parse_user_input(commands[i])
            self.assertEqual(cmd.get_command_tag() == commands[i], True)
            self.assertEqual(tokens == [], True)
            self.assertEqual(message == "", True)
        cmd, tokens, message = command_manager.parse_user_input("blabla")
        self.assertEqual(cmd == None, True)
        self.assertEqual(tokens == None, True)
        self.assertEqual(message == "Command not supported: ", True)

    def test_make_command_dict(self):
        command_manager = CommandManager()
        a, b, c, d, e, f = Quit(), GoDown(), GoUp(), GoLeft(), GoRight(), Skip()
        dic = command_manager.make_commands_dict([a, b, c, d, e, f])
        manual_dic = {"quit": a,
                      "go-down": b,
                      "go-up": c,
                      "go-left": d,
                      "go-right": e,
                      "skip": f}

        self.assertEqual(dic, manual_dic)

    def test_eval_command(self):
        command_manager = CommandManager()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))
        finished, message = command_manager.eval_command(Quit(), [], labyrinth, player)
        self.assertEqual(finished, True)
        self.assertEqual(message, "Finished")

        finished, message = command_manager.eval_command(Quit(), ["a"], labyrinth, player)
        self.assertEqual(finished, False)
        self.assertEqual(message, "Invalid number of args. Expected: 0, got: 1")


if __name__ == '__main__':
    unittest.main()
