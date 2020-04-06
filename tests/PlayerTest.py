import unittest

from impl.Player import Player
from impl.labyrinth.Cell import Cell
from impl.labyrinth.Labyrinth import Labyrinth
from impl.objects.Treasure import Treasure


class PlayerTest(unittest.TestCase):
    def test_add_objects_and_get_objects_and_remove_object(self):
        player = Player(0, 0)
        t = Treasure()
        self.assertEqual(len(player.get_objects()), 0)
        player.add_object(t)
        self.assertEqual(len(player.get_objects()), 1)
        player.remove_object(t)
        self.assertEqual(len(player.get_objects()), 0)

    def test_get_current_cell(self):
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

        self.assertEqual(isinstance(player.get_current_cell(labyrinth), Cell), True)

    def test_get_set_pos(self):
        player = Player(0, 0)
        x, y = player.get_pos()
        self.assertEqual(x == 0, True)
        self.assertEqual(y == 0, True)
        player.set_pos(1, 1)
        x, y = player.get_pos()
        self.assertEqual(y == 1, True)
        self.assertEqual(x == 1, True)

    def test_move_up(self):
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))

if __name__ == '__main__':
    unittest.main()
