import os

from impl.labyrinth.cells.CellEmpty import CellEmpty
from impl.labyrinth.cells.CellMonolith import CellMonolith
from impl.labyrinth.cells.CellNoWall import CellNoWall
from impl.labyrinth.cells.CellStart import CellStart
from impl.labyrinth.cells.CellTreasure import CellTreasure
from impl.labyrinth.cells.CellWall import CellWall
from impl.labyrinth.cells.CellWormhole import CellWormhole
from impl.objects.Treasure import Treasure


class GameLoader:

    def __init__(self):
        pass

    def load_game(self, args, player, labyrinth):
        file = self.open_file(args)
        lines = file.readlines()

        # get coordonates
        pos_x, pos_y = map(int, lines[0].replace("\n", "").split(","))

        inventory = lines[1].replace("\n", "").split(",")
        object_inventory = self.get_inventory_objects_from_symbols(inventory)

        lab = self.get_labyrinth_from_symbols(lines[2:])
        lab_size = (len(lab[0]) - 1 )/ 2

        player.set_pos(pos_x, pos_y)
        player.set_objects(object_inventory)
        labyrinth.set_size(lab_size)
        labyrinth.set_labyrinth(lab)
        return True

    def open_file(self, args):
        file_exists = os.path.exists("saved_games/" + args[0] + ".txt")
        if not file_exists:
            raise FileExistsError()
        else:
            try:
                return open("saved_games/" + args[0] + ".txt", "r")
            except Exception:
                raise IOError

    def get_inventory_objects_from_symbols(self, inventory_symbols):
        comparison_dict = {
            "T": Treasure()
        }
        inventory_objects = []
        for sym in inventory_symbols:
            inventory_objects.append(comparison_dict[sym])
        return inventory_objects

    def get_labyrinth_from_symbols(self, laby_symbols):
        comparison_dict = {
            '*': CellEmpty(),
            'M': CellMonolith(),
            '-': CellNoWall(),
            'S': CellStart(),
            'T': CellTreasure(),
            'W': CellWall()
        }
        wormhole_number = self.find_wormhole_number(laby_symbols)
        laby = []
        for line in laby_symbols:
            row = []
            for sym in line.replace("\n", ""):
                if sym.isnumeric():
                    row.append(CellWormhole(int(sym), wormhole_number))
                else:
                    row.append(comparison_dict[sym])
            laby.append(row)
        return laby

    def find_wormhole_number(self, laby_symbols):
        nb = 0
        for line in laby_symbols:
            for sym in line:
                if sym.isnumeric():
                    nb += 1
        return nb