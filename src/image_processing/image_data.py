from math.vectors import Vec3


class Color:
    """specifies a data structure that stores color in rgb 256 format.""" 
    def __init__(self, rgb: Vec3):
        """Converts Vec3 coordinates to the range [0; 255]""" 


class ImageData: 
    """Specifies a data structure that stores the colors of an image and provides pixel-by-pixel access to it."""
    def __init__(self, width: int, height: int, colors: list): 
        """The size of the colors array have to be equal to width * height."""
    
    def get_pixel(self, pixel_x: int, pixel_y: int) -> Color: 
        """Get the color of a pixel with coordinates (pixel_x, pixel_y)."""
