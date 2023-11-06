from time import sleep
from render.cell import Cell_render

class Maze_render:
    def __init__(
            self,
            maze,
            x1,
            y1,
            cell_size,
            win
            ):
            self.maze = maze
            self.x1 = x1
            self.y1 = y1
            self.cell_size = cell_size
            self.win = win
            self._draw_grid()
            self.draw_solution()

    def _draw_grid(self):
        grid = self.maze.grid
        for i in range(self.maze.num_rows):
            for j in range(self.maze.num_cols):
                cell = self.__renderer_of(grid[i][j])
                self._draw_cell(cell)

    def _draw_cell(self, cell):
        self.win.draw_cell(cell, "black")
        self._animate()

    def draw_solution(self):
        cells = self.__renderers_from(self.maze._visited)
        for i in range(len(cells) - 1):
            j = i
            while not self.__cells_are_adjacent(cells[j], cells[i+1]) \
                    and j >= 0:
                if self.__cells_are_adjacent(cells[j], cells[j - 1]):
                    self.win.draw_move(cells[j], cells[j-1], undo=True)
                j -= 1

            self.win.draw_move(cells[j], cells[i + 1])
            self._animate()

    def __cells_are_adjacent(self, cell, other):
        return cell.cell.is_adjacant_to(other.cell)

    def __renderer_of(self, cell):
        return Cell_render(cell, self.cell_size, self.x1, self.y1)

    def __renderers_from(self, cells):
        return list(map(
            lambda cell: self.__renderer_of(cell),
            cells
            ))

    def _animate(self):
        self.win.redraw()
        sleep(0.01)
