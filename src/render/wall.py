from line import Line

class Wall:
    def __init__(self, p1, p2, exist):
        self.line = Line(p1, p2)
        self.exist = exist

    def draw(self, canvas, fill_color):
        self.line.draw(canvas, fill_color)
