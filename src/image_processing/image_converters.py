from src.image_processing.image_converter_base import ImageConverterBase
from src.image_processing.image_data import ImageData
from PIL import Image


class UnicodeConverter(ImageConverterBase):
    """Converts an image to a pseudographic text format."""
    def __init__(self, gradient: str):
        """Gradient is a string of characters arranged by increasing brightness."""
    
    def convert(self, image_data: ImageData) -> str:
        pass

        
class PNGConverter(ImageConverterBase):
    "Converts an image to a png file." 
    def __init__(self):
        pass

    def convert(self, image_data: ImageData, save_path: str):
        res_image = Image.new("RGB", (image_data.width, image_data.height), (0, 0, 0))
        pixels = res_image.load()

        for x in image_data.width:
            for y in image_data.height:
                pixel_color = image_data.get_pixel(x, y)
                pixels[x, y] = (pixel_color.r, pixel_color.g, pixel_color.b)

        res_image.save(save_path)