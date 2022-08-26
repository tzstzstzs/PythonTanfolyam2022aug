
from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def main():
    print(Color.RED.value)

##############################################################################

if __name__ == "__main__":
    main()
