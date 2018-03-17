from enum import Enum


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    RIGHT = "R"
    LEFT = "L"
    DESCEND = "Z"
    DESCEND_UP = "ZU"
    DESCEND_DOWN = "ZD"
    DESCEND_RIGHT = "ZR"
    DESCEND_LEFT = "ZL"
    PULL = "P"
    PULL_UP = "PU"
    PULL_DOWN = "PD"
    PULL_RIGHT = "PR"
    PULL_LEFT = "PL"
