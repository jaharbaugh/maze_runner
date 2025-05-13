from point_line import *
class Cell():
    def __init__(self, win, 
                 x1, x2, y1, y2,
                 has_right=True, has_left=True,
                 has_top=True, has_bottom=True):
        
        self.has_right_wall = has_right
        self.has_left_wall = has_left
        self.has_top_wall = has_top
        self.has_bottom_wall = has_bottom

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.win = win

    def draw(self):
        if self.has_left_wall is True:
            start_point = Point(self.x1, self.y1)
            end_point = Point(self.x1, self.y2)
            left = Line(start_point, end_point)
            left.draw(self.win.canvas, "black")
        if self.has_right_wall is True:
            start_point = Point(self.x2, self.y1)
            end_point = Point(self.x2, self.y2)
            right = Line(start_point, end_point)
            right.draw(self.win.canvas, "black")
        if self.has_top_wall is True:
            start_point = Point(self.x1, self.y1)
            end_point = Point(self.x2, self.y1)
            top = Line(start_point, end_point)
            top.draw(self.win.canvas, "black")
        if self.has_bottom_wall is True:
            start_point = Point(self.x1, self.y2)
            end_point = Point(self.x2, self.y2)
            bottom = Line(start_point, end_point)
            bottom.draw(self.win.canvas, "black")