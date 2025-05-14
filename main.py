from tkinter import Tk, BOTH, Canvas
from window import *
from point_line import *
from cell import *

win = Window(800, 600)

c1 = Cell(win, 50, 50, 100, 100, True, True, True, False)
c1.draw()

c2 = Cell(win, 100, 50, 150, 100, True, True, False, True)
c2.draw()


c1.draw_move(c2, False)

win.wait_for_close()




