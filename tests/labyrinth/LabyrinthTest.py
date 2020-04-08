import unittest

from impl.labyrinth.Labyrinth import Labyrinth


class LabyrinthTest(unittest.TestCase):

    def test_generate_random_exit(self):
        laby = Labyrinth(4)
        laby.generate_labyrinth()

        e_x, e_y = laby.generate_random_exit()

        self.assertEqual((e_x == 0 or e_x == 8) or (e_y == 8 or e_y == 0), True)

    def test_initialize_special_cells(self):
        laby = Labyrinth(4)
        laby.generate_labyrinth()
        self.assertEqual(len(laby.initialize_special_cells()), 5)

        laby = Labyrinth(8)
        laby.generate_labyrinth()
        self.assertEqual(len(laby.initialize_special_cells()), 6)

        laby = Labyrinth(10)
        laby.generate_labyrinth()
        self.assertEqual(len(laby.initialize_special_cells()), 7)

    def test_generate_labyrinth_and_export(self):
        laby = Labyrinth(4)
        laby.generate_labyrinth()
        export = laby.export_labyrinth()

        print(export.count("*"))
        print(export.count("S"))
        print(export.count("T"))
        self.assertEqual(export.count("S"), 1)
        self.assertEqual(export.count("T"), 1)
        self.assertEqual(export.count("M"), 31)
        self.assertEqual(export.count("*"), 11)

if __name__ == '__main__':
    unittest.main()
