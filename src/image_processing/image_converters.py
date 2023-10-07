from image_processing.image_converter_base import ImageConverterBase
from image_processing.image_data import ImageData

class UnicodeConverter(ImageConverterBase):
    """Converts an image to a pseudographic text format."""
    def __init__(gradient: str):
        """Gradient is a string of characters arranged by increasing brightness."""
    
    def convert(image_data: ImageData) -> str:
        pass


class PNGConverter(ImageConverterBase):
    "Converts an image to a png file." 
    def __init__():
        pass

    def convert(image_data: ImageData, save_path: str):
        pass