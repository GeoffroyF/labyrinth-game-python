from pathlib import Path
import os


class GameSaver:
    """Class to save the Game"""

    def __init__(self):
        pass

    def save_game(self, args, player, labyrinth):
        """Main method to create a save file"""
        try:
            file = self.create_dir_and_file(args)
            pos_x, pos_y = player.get_pos()
            objects = ",".join([str(o) for o in player.get_objects()])
            labyrinth_export = labyrinth.export_labyrinth()

            file.write(str(pos_x) + "," + str(pos_y) + "\n")
            file.write(objects + "\n")
            file.write(labyrinth_export)
        except FileExistsError:
            raise FileExistsError
        except IOError:
            raise IOError
        except Exception:
            raise Exception

    def create_dir_and_file(self, args):
        """ If the File doesn't exist, it is created. Otherwise it can be overwritten"""
        Path("saved_games").mkdir(parents=True, exist_ok=True)

        file_exists = os.path.exists("saved_games/" + args[0] + ".txt")
        if file_exists:
            overwrite = ""
            while overwrite != "yes" and overwrite != "no":
                overwrite = input("File already exists, do you want to overwrite ? [yes/no] : ")
            if overwrite == "no":
                raise FileExistsError()
        try:
            return open("saved_games/" + args[0] + ".txt", "w")
        except Exception:
            raise IOError
