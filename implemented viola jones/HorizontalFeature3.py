from Feature import Feature

class HorizontalFeature3(Feature):
    def __init__(self, x: int, y: int, width: int, height: int):                       #   - + -
        super().__init__(x, y, width, height)                                          #   - + -
        tw = width // 3                                                                #   - + -
        self.coords_x = [x,        x + tw,    x,          x + tw,           
                         x + tw,   x + 2*tw,  x + tw,     x + 2*tw,
                         x + 2*tw, x + width, x + 2*tw,   x + width]
        self.coords_y = [y,        y,         y + height, y + height,
                         y,        y,         y + height, y + height,
                         y,        y,         y + height, y + height]
        self.coeffs   = [-1,       1,         1,         -1,                            #  1 ---> the value that will be added using integral matrix
                          1,      -1,        -1,          1,                            # -1 ---> the value that will be removed using integral matrix
                         -1,       1,         1,         -1]