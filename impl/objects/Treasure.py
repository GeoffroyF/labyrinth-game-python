from impl.objects.Object import LabyrinthObject


class Treasure(LabyrinthObject):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "T"
