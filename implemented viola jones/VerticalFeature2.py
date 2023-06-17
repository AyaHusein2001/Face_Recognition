from Feature import Feature

class VerticalFeature2(Feature):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)
        halfHeight = height // 2                                                                    #   -----
        self.coords_x = [x,      x + width,  x,          x + width,                         #   +++++    
                         x,      x + width,  x,          x + width]
        self.coords_y = [y,      y,          y + halfHeight,     y + halfHeight,
                         y + halfHeight, y + halfHeight,     y + height, y + height]
        self.coeffs   = [-1,     1,          1,         -1,                                 #  1 ---> the value that will be added using integral matrix        
                         1,     -1,         -1,          1]                                 # -1 ---> the value that will be removed using integral matrix