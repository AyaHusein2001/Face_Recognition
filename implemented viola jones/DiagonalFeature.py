from Feature import Feature

class DiagonalFeature(Feature):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)                                    
        halfWidth = width //  2                                                                           #   + -
        halfHeight = height // 2                                                                           #   - + 
        self.coords_x = [x,      x + halfWidth,     x,          x + halfWidth,     
                         x + halfWidth, x + width,  x + halfWidth,     x + width,
                         x,      x + halfWidth,     x,          x + halfWidth,     
                         x + halfWidth, x + width,  x + halfWidth,     x + width]
        self.coords_y = [y,      y,          y + halfHeight,     y + halfHeight,     
                         y,      y,          y + halfHeight,     y + halfHeight,
                         y + halfHeight, y + halfHeight,     y + height, y + height, 
                         y + halfHeight, y + halfHeight,     y + height, y + height]
        self.coeffs   = [1,     -1,         -1,          1,          
                         -1,     1,          1,         -1,                              #  1 ---> the value that will be added using integral matrix
                         -1,     1,          1,         -1,                              # -1 ---> the value that will be removed using integral matrix 
                          1,    -1,         -1,          1]