import random
from core.cell import Cell
class Maze:
    def __init__(
            self,
            num_rows,
            num_cols,
            ):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = []
        self._visited = []
        self._create_grid()
        self._visited = []
        self.solve()

    def _create_grid(self):
        for i in range(self.num_rows):
            self._grid.append([])
            for j in range(self.num_cols):
                self._grid[i].append(Cell(i,j))
        self.first._break_wall("top")
        self.last._break_wall("bottom")
        self._break_walls_random(self.first)

    def solve(self):
        return self.solve_random(self.first)

    def solve_random(self, cell):
        self._visited.append(cell)
        if cell == self.last:
            return True
        directions = self.__get_filtered_directions(cell)
        for direction in directions:
            if cell.has_open_path_to(direction):
                if(self.solve_random(direction)):
                    return True
        return False

    def _break_walls_random(self, cell):
        self._visited.append(cell)
        while True:
            directions = self.__get_filtered_directions(cell)
            if len(directions) == 0:
                return
            next_cell = random.choice(directions)
            cell.break_connecting_wall_to(next_cell)
            self._break_walls_random(next_cell)
        
    def __get_filtered_directions(self, cell):
        return list(filter(
            lambda cell: cell not in self._visited,
            self.get_adjacent_cells(cell)
            ))

    @property
    def first(self):
        return self.grid[0][0]

    @property
    def last(self):
        return self.grid[self.num_rows - 1][self.num_cols - 1]
    @property
    def grid(self):
        return self._grid

    
    def get_cell(self, row, col):
        if self._grid[row][col] is None:
            raise IndexError
        return self._grid[row][col]

    def get_cell_above(self, cell):
        if cell.row > 0:
            return self.get_cell(cell.row - 1, cell.col)
        return None

    def get_cell_below(self, cell):
        if cell.row < self.num_rows - 1:
            return self.get_cell(cell.row + 1, cell.col)
        return None

    def get_cell_left_of(self, cell):
        if cell.col > 0:
            return self.get_cell(cell.row, cell.col - 1)
        return None

    def get_cell_right_of(self, cell):
        if cell.col < self.num_cols - 1:
            return self.get_cell(cell.row, cell.col + 1)
        return None

    def get_adjacent_cells(self, cell):
        cells = [
                self.get_cell_below(cell),
                self.get_cell_above(cell),
                self.get_cell_left_of(cell),
                self.get_cell_right_of(cell)
                ]
        return filter(
                lambda cell: cell is not None,
                cells
                )
