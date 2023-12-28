from src.renderer.renderer import Renderer
from src.scene_components.scene import Scene
from src.scene_components.bodies.body import Body
from src.scene_components.bodies.shapes.shapes import Sphere, Plane, Disk, Cylinder, Box, ClampedCylinder
from src.scene_components.bodies.material import Material
from src.scene_components.lights.light_sources import DirectedLight
from src.scene_components.lights.lighting import Lighting
from src.renderer.cameras import PerspectiveCamera
from src.math_tools.vectors import Vec3
from src.image_processing.image_converters import PNGConverter

scene = Scene(
    PerspectiveCamera(Vec3(0, 0, 0)),
    Lighting(Vec3(0.2), [DirectedLight(Vec3(0.5, 0.5, -0.5), Vec3(250, 250, 250))], Vec3(90, 200, 240)),
    [   
        Body(
            Sphere(Vec3(0, 0, 5), 0.5),
            Material(Vec3(240, 128, 0), 0, 1),
        ),

        Body(
            Sphere(Vec3(1.3, 0, 5), 0.5),
            Material(Vec3(19, 232, 97), 0, 1),
        ),

        Body(
            Plane(Vec3(0, -0.5, 0)),
            Material(Vec3(220, 220, 220), 0, 1),
        ),

        # Body(
        #     Disk(Vec3(-1.3, 0, 5), 0.5, Vec3(1, 1, -1)),
        #     Material(Vec3(19, 97, 232), 0, 1),
        # ),

        # Body(
        #     Cylinder(Vec3(-1.3, 0, 5), 0.5),
        #     Material(Vec3(19, 97, 232), 0, 1),
        # ),

        # Body(
        #     Box(Vec3(-1.3 - 0.5, -0.5, 5 - 0.5), Vec3(1)),
        #     Material(Vec3(19, 97, 232), 0, 1),
        # ),

        # Body(
        #     ClampedCylinder(Vec3(-1.3, -0.5, 5), 0.5, 0.1),
        #     Material(Vec3(19, 97, 232), 0, 1),
        # ),
    ],
)

renderer = Renderer()
image_data = renderer.render(scene, 320, 180)

converter = PNGConverter()
converter.convert(image_data, "./res.png")