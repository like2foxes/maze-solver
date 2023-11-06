from core.wall import Wall
class Cell:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__walls = { 
                        "left": Wall(), 
                        "right": Wall(), 
                        "top": Wall(), 
                        "bottom": Wall()
                        }

    def has_open_path_to(self, other):
        if self.is_below(other):
            return not self.walls["top"].exists and not other.walls["bottom"].exists
        if self.is_above(other):
            return not self.walls["bottom"].exists and not other.walls["top"].exists
        if self.is_left_of(other):
            return not self.walls["right"].exists and not other.walls["left"].exists
        if self.is_right_of(other):
            return not self.walls["left"].exists and not other.walls["right"].exists

    def is_above(self, other):
        if self.row == other.row - 1 and self.col == other.col:
            return True
        return False

    def is_below(self, other):
        if other.is_above(self):
            return True
        return False

    def is_left_of(self, other):
        if self.col == other.col - 1 and self.row == other.row:
            return True
        return False

    def is_right_of(self, other):
        if other.is_left_of(self):
            return True
        return False

    def is_adjacant_to(self, other):
        return self.is_below(other) or \
                self.is_above(other) or \
                self.is_left_of(other) or \
                self.is_right_of(other)

    @property
    def walls(self):
        return self.__walls

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    @property
    def left(self):
        return self.__walls["left"]

    @property
    def right(self):
        return self.__walls["right"]

    @property
    def top(self):
        return self.__walls["top"]

    @property
    def bottom(self):
        return self.__walls["bottom"]

    def break_connecting_wall_to(self, other):
        if self.is_below(other):
            self._break_wall("top")
            other._break_wall("bottom")
        elif self.is_above(other):
            self._break_wall("bottom")
            other._break_wall("top")
        elif self.is_right_of(other):
            self._break_wall("left")
            other._break_wall("right")
        elif self.is_left_of(other):
            self._break_wall("right")
            other._break_wall("left")
        else:
            raise ValueError

    def _break_wall(self, wall):
        if self.__walls[wall] is None:
            raise Exception("undefined wall")
        self.__walls[wall]._break()

    def _create_wall(self, wall):
        if self.__walls[wall] is None:
            raise Exception("undefined wall")
        self.__walls[wall]._create()

    def __str__(self):
        return f"cell at ({self.row},{self.col}):\nleft - {self.left}, right - {self.right}, top - {self.top}, bottom - {self.bottom})"

    def __eq__(self, other):
        return isinstance(other, Cell) and \
                self.col == other.col and \
                self.row == other.row
