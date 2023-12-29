from src.image_processing.image_converter_base import ImageConverterBase
from src.image_processing.image_data import ImageData
from PIL import Image


class UnicodeConverter(ImageConverterBase):
    """Converts an image to a pseudographic text format."""

    def __init__(self, gradient: str):
        """Gradient is a string of characters arranged by increasing brightness."""
        self.gradient = gradient

    def convert(self, image_data: ImageData) -> str:
        rows = []

        for y in range(image_data.height):
            row = ""

            for x in range(image_data.width):
                pixel_color = image_data.get_pixel(x, y)

                brightness = (pixel_color.r + pixel_color.g + pixel_color.b) / 3 / 255
                gradient_index = max(
                    min(int(brightness * len(self.gradient)), len(self.gradient) - 1), 0
                )
                row += self.gradient[gradient_index]

            rows.append(row)

        return "\n".join(rows)


class PNGConverter(ImageConverterBase):
    "Converts an image to a png file."

    def __init__(self):
        pass

    def convert(self, image_data: ImageData, save_path: str):
        res_image = Image.new("RGB", (image_data.width, image_data.height), (0, 0, 0))
        pixels = res_image.load()

        for x in range(image_data.width):
            for y in range(image_data.height):
                pixel_color = image_data.get_pixel(x, y)
                pixels[x, y] = (pixel_color.r, pixel_color.g, pixel_color.b)

        res_image.save(save_path)
