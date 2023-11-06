from render.line import Line
from render.point import Point

class Cell_render:
    def __init__(self, cell, size, startx, starty):
        self.__cell = cell
        self.__size = size
        self.__startx = startx
        self.__starty = starty

    @property
    def cell(self):
        return self.__cell
    @property
    def x1(self):
        return self.__cell.col * self.__size + self.__startx

    @property
    def x2(self):
        return self.x1 + self.__size

    @property
    def y1(self):
        return self.__cell.row * self.__size + self.__starty

    @property
    def y2(self):
        return self.y1 + self.__size

    def wall_to_line(self, side):
        if side == "left":
            return Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        if side == "right":
            return Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        if side == "top":
            return Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        if side == "bottom":
            return Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
        raise NameError("no such side")

    @property
    def center(self):
        centerx = (self.x2 + self.x1) // 2
        centery = (self.y2 + self.y1) // 2
        return Point(centerx, centery)

    def draw(self, canvas, fill_color, bg_color):
        walls = self.__cell.walls
        for side in walls:
            color = fill_color if walls[side].exists else bg_color
            line = self.wall_to_line(side)
            line.draw(canvas, color)

    def draw_move(self,canvas, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        fill_color = "grey" if undo else "red"
        line.draw(canvas, fill_color)
