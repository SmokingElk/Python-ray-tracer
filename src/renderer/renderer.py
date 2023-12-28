from src.image_processing.image_data import ImageData, Color
from src.scene_components.scene import Scene
from src.renderer.ray_model import RayModel

class Renderer:
    """performs image rendering.""" 
    def __init__(self):
        self._scene = None
        self._width = 0
        self._height = 0

    def _reset(self): 
        """reset to the initial state (called before starting a new render)."""
        self._scene = None
        self._width = 0
        self._height = 0

    def _get_pixel_color(self, x: int, y: int) -> Color:
        """determines the color of a pixel by its screen coordinates""" 
        ro, rd = self._scene.camera.viewport(x, y, self._width, self._height, self._pixel_aspect)
        color_vec = self._ray_model.trace_ray(ro, rd)

        color = Color(color_vec)
        return color
    
    def render(self, scene: Scene, width: int, height: int, pixel_aspect: float=1) -> ImageData:
        """Converts a scene model into an image."""
        self._scene = scene
        self._width = width
        self._height = height
        self._pixel_aspect = pixel_aspect
        self._ray_model = RayModel(scene.lighting, scene.scene_objects)

        pixels = []

        for y in range(height):
            for x in range(width):
                pixelColor = self._get_pixel_color(x, y)
                pixels.append(pixelColor)

        image = ImageData(width, height, pixels)
        return image
    