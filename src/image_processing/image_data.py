from src.math_tools.vectors import Vec3
from src.math_tools.utilities import limit

class Color:
    """specifies a data structure that stores color in rgb 256 format.""" 
    def __init__(self, rgb: Vec3):
        """Converts Vec3 coordinates to the range [0; 255]"""
        self.r = int(limit(rgb.x, 0, 1) * 255)
        self.g = int(limit(rgb.y, 0, 1) * 255)
        self.b = int(limit(rgb.z, 0, 1) * 255)


class ImageData: 
    """Specifies a data structure that stores the colors of an image and provides pixel-by-pixel access to it."""
    def __init__(self, width: int, height: int, colors: list): 
        """The size of the colors array have to be equal to width * height."""
        self.width = width
        self.height = height
        self._colors = colors
    
    def get_pixel(self, pixel_x: int, pixel_y: int) -> Color: 
        """Get the color of a pixel with coordinates (pixel_x, pixel_y)."""
        pixel_index = pixel_y * self.height + pixel_x
        return self._colors[pixel_index]

