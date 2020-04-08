import unittest

from impl.Player import Player
from impl.command_manager.commands import Quit, GoUp, GoDown, GoLeft, GoRight, Skip, ShowLabyrinth, GoUpShort, \
    GoDownShort, GoLeftShort, GoRightShort, SaveGame, LoadGame
from impl.labyrinth.Labyrinth import Labyrinth


class CommandsTest(unittest.TestCase):
    def test_quit(self):
        cmd = Quit()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "quit")
        self.assertEqual(cmd.get_args_count(), 0)

        finished, message = cmd.evaluate([], labyrinth, player)
        self.assertEqual(finished, True)
        self.assertEqual(message, "Finished")

    def test_go_up(self):
        cmd = GoUp()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "go-up")
        self.assertEqual(cmd.get_args_count(), 0)

        won, message = cmd.evaluate([], labyrinth, player)
        self.assertEqual(isinstance(won, bool), True)
        self.assertEqual(isinstance(message, str), True)

    def test_go_down(self):
        cmd = GoDown()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "go-down")
        self.assertEqual(cmd.get_args_count(), 0)

        won, message = cmd.evaluate([], labyrinth, player)
        self.assertEqual(isinstance(won, bool), True)
        self.assertEqual(isinstance(message, str), True)

    def test_go_left(self):
        cmd = GoLeft()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "go-left")
        self.assertEqual(cmd.get_args_count(), 0)

        won, message = cmd.evaluate([], labyrinth, player)
        self.assertEqual(isinstance(won, bool), True)
        self.assertEqual(isinstance(message, str), True)

    def test_go_right(self):
        cmd = GoRight()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "go-right")
        self.assertEqual(cmd.get_args_count(), 0)

        won, message = cmd.evaluate([], labyrinth, player)
        self.assertEqual(isinstance(won, bool), True)
        self.assertEqual(isinstance(message, str), True)

    def test_skip(self):
        cmd = Skip()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "skip")
        self.assertEqual(cmd.get_args_count(), 0)

        won, message = cmd.evaluate([], labyrinth, player)
        self.assertEqual(won, False)
        self.assertEqual(message, "step executed")

    def test_show(self):
        cmd = ShowLabyrinth()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "show")
        self.assertEqual(cmd.get_args_count(), 0)

        won, message = cmd.evaluate([], labyrinth, player)
        self.assertEqual(won, False)
        self.assertEqual(message, "labyrinth shown")

    def test_short_commands(self):
        self.assertEqual(GoUpShort().get_command_tag(), "z")
        self.assertEqual(GoDownShort().get_command_tag(), "s")
        self.assertEqual(GoLeftShort().get_command_tag(), "q")
        self.assertEqual(GoRightShort().get_command_tag(), "d")

    def test_save(self):
        cmd = SaveGame()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "save")
        self.assertEqual(cmd.get_args_count(), 1)

    def test_load(self):
        cmd = LoadGame()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(cmd.get_command_tag(), "load")
        self.assertEqual(cmd.get_args_count(), 1)


if __name__ == '__main__':
    unittest.main()
