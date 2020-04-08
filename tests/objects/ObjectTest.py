import unittest

from impl.objects.Treasure import Treasure


class ObjectTest(unittest.TestCase):

    def test_something(self):
        self.assertEqual(str(Treasure()), "T")


if __name__ == '__main__':
    unittest.main()
