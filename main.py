from renderer.renderer import Renderer
from scene_components.scene import Scene
from scene_components.bodies.shapes.shapes import Sphere
from scene_components.bodies.material import Material
from scene_components.lights.light_sources import DirectedLight
from scene_components.lights.lighting import Lighting
from renderer.cameras import PerspectiveCamera
from math_tools.vectors import Vec3
from image_processing.image_converters import PNGConverter

scene = Scene(
    PerspectiveCamera(Vec3(0)),
    Lighting(Vec3(0.1), [DirectedLight(Vec3(0.5, 0.5, -0.5))]),
    [
        Sphere(Vec3(0, 0, 5), 0.5),
    ],
)

renderer = Renderer()
image_data = renderer.render(scene, 320, 180)

converter = PNGConverter()
converter.convert(image_data, "./res.png")