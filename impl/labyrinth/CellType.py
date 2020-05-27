from enum import Enum


class CellType(Enum):
    EMPTY = "empty"
    STARTING_CELL = "starting_cell"
    TREASURE = "treasure"
    WALL = "wall"
    MONOLITH = "monolith"
    NO_WALL = "no_wall"
    WORMHOLE = "wormhole"
    RIVER = "river"
    BEAR = "bear"
