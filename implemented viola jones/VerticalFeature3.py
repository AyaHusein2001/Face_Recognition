from Feature import Feature

class VerticalFeature3(Feature):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)
        th = height // 3                                                                  #   ---------
        self.coords_x = [x,        x + width,  x,          x + width,                     #   +++++++++
                         x,        x + width,  x,          x + width,                     #   ---------  
                         x,        x + width,  x,          x + width]
        self.coords_y = [y,        y,          y + th,     y + th,
                         y + th,   y + th,     y + 2*th,   y + 2*th,
                         y + 2*th, y + 2*th,   y + height, y + height]
        self.coeffs   = [-1,        1,         1,         -1,                              #  1 ---> the value that will be added using integral matrix
                          1,       -1,        -1,          1,                              # -1 ---> the value that will be removed using integral matrix
                         -1,        1,         1,         -1]