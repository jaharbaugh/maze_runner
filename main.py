from tkinter import Tk, BOTH, Canvas
from window import *
from point_line import *

win = Window(800, 600)
x = Point(100, 100)
y = Point(500, 100)

line = Line(x, y)
win.draw_line(line, "black")

win.wait_for_close()




