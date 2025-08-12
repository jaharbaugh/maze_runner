from cell import *
from window import *
import time
import random

class Maze():
    def __init__(self,
                 x1, y1, num_rows, num_cols,
                 cell_size_x, cell_size_y, win=None,
                 seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def _create_cells(self):
        self.__cells = []
        for i in range(0, self.num_rows):
            row = []
            for j in range(0, self.num_cols):
                row.append(None)
            self.__cells.append(row)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        


        if self.__cells[i][j] is not None:
            if self.win is not None:
                self.__cells[i][j].draw()
        else:
            self.__cells[i][j] = Cell(x1, x2, y1, y2, True, True, True, True, self.win)
            if self.win is not None:
                self.__cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
        time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall= False
        self.__cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0,0)
        self._draw_cell(self.num_rows -1, self.num_cols -1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            to_visit = []
            if i-1 >= 0 and self.__cells[i-1][j].visited is False:
                to_visit.append((i-1,j))
            if j-1 >= 0 and self.__cells[i][j-1].visited is False:
                to_visit.append((i, j-1))
            if i+1 <= self.num_rows-1 and self.__cells[i+1][j].visited is False:
                to_visit.append((i+1, j))
            if j+1 <= self.num_cols-1 and self.__cells[i][j+1].visited is False:
                to_visit.append((i, j+1))

            if to_visit == []:
                self._draw_cell(i,j)
                return
            else:
                next_cell = random.choice(to_visit)
                next_i = next_cell[0]
                next_j = next_cell[1]
                if next_i < i:
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[next_i][next_j].has_bottom_wall = False
                if next_i > i:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[next_i][next_j].has_top_wall = False
                if next_j < j:
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[next_i][next_j].has_right_wall = False
                if next_j > j:
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[next_i][next_j].has_left_wall = False    
                self.__break_walls_r(next_i,next_j)
        
    def __reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited=False

