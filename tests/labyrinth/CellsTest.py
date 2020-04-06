import unittest

from impl.Player import Player
from impl.labyrinth.CellType import CellType
from impl.labyrinth.Labyrinth import Labyrinth
from impl.labyrinth.cells.CellEmpty import CellEmpty
from impl.labyrinth.cells.CellMonolith import CellMonolith
from impl.labyrinth.cells.CellNoWall import CellNoWall
from impl.labyrinth.cells.CellStart import CellStart
from impl.labyrinth.cells.CellTreasure import CellTreasure
from impl.labyrinth.cells.CellWall import CellWall
from impl.labyrinth.cells.CellWormhole import CellWormhole
from impl.objects.Treasure import Treasure


class CommandManagerTest(unittest.TestCase):

    def test_cell_to_str(self):
        self.assertEqual(str(CellEmpty()), "*")
        self.assertEqual(str(CellMonolith()), "M")
        self.assertEqual(str(CellNoWall()), "-")
        self.assertEqual(str(CellStart()), "S")
        self.assertEqual(str(CellTreasure()), "T")
        self.assertEqual(str(CellWall()), "W")
        self.assertEqual(str(CellWormhole(1, 2)), "1")

    def test_cell_type(self):
        self.assertEqual(CellEmpty().get_cell_type(), CellType.EMPTY)
        self.assertEqual(CellMonolith().get_cell_type(), CellType.MONOLITH)
        self.assertEqual(CellNoWall().get_cell_type(), CellType.NO_WALL)
        self.assertEqual(CellStart().get_cell_type(), CellType.STARTING_CELL)
        self.assertEqual(CellTreasure().get_cell_type(), CellType.TREASURE)
        self.assertEqual(CellWall().get_cell_type(), CellType.WALL)
        self.assertEqual(CellWormhole(1, 2).get_cell_type(), CellType.WORMHOLE)

    def test_treasure_execution(self):
        cell_treasure = CellTreasure()
        labyrinth = Labyrinth(4)
        player_pos_x, player_pos_y = labyrinth.generate_labyrinth()
        player = Player(int(player_pos_x), int(player_pos_y))
        x, y = find_treasure(labyrinth)
        player.set_pos(x, y)

        print(has_treasure(labyrinth))
        self.assertEqual(has_treasure(labyrinth), True)
        cell_treasure.execute_action(labyrinth, player)
        self.assertEqual(has_treasure(labyrinth), False)
        self.assertEqual(isinstance(player.get_objects()[0], Treasure), True)


if __name__ == '__main__':
    unittest.main()


def has_treasure(labyrinth):
    for i in labyrinth.get_labyrinth():
        for j in i:
            if j.get_cell_type() == CellType.TREASURE:
                return True
    return False


def find_treasure(labyrinth):
    for i in range(labyrinth.get_size() * 2 + 1):
        for j in range(labyrinth.get_size() * 2 + 1):
            if labyrinth.get_labyrinth()[i][j].get_cell_type() == CellType.TREASURE:
                return int((j - 1) / 2), int((i - 1) / 2)
