from image_processing.image_data import ImageData, Color
from scene_components.scene import Scene


class Renderer:
    """performs image rendering.""" 
    def __init__(self):
        pass

    def _reset(self): 
        """reset to the initial state (called before starting a new render)."""

    def _get_pixel_color(self, x: int, y: int) -> Color:
        """determines the color of a pixel by its screen coordinates""" 
    
    def render(self, scene: Scene) -> ImageData:
        """Converts a scene model into an image."""