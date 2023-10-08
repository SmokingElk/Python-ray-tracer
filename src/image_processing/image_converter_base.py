from image_processing.image_data import ImageData


class ImageConverterBase:
    """Converting ImageData to another format."""
    def __init__(self):
        pass

    def average(self, x: int, y: int, sizeX: int, sizeY: int):
        """Calculates the average color of the image area from the size (sizeX, sizeY) with coordinates (x, y)."""
        
    def convert(self, image_data: ImageData):
        """performs the conversion in image_data to the appropriate format."""