from tkinter import Tk, BOTH, Canvas
from window import *
from point_line import *
from cell import *

win = Window(800, 600)

c1 = Cell(win, 100, 500, 100, 500, True, True, True, False)
c1.draw()

win.wait_for_close()




