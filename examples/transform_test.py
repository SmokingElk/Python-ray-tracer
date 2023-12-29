import sys
import os
sys.path.append(os.getcwd())

from src.engine import (
    Vec3,
    Renderer,
    PNGConverter,
    PerspectiveCamera,
    Scene, Lighting, Body, Material,
    Sphere, Plane, Box, Cylinder, ClampedCylinder,
    DirectedLight, PointLight,
    gamma_correction,
)

scene = Scene(
    PerspectiveCamera(Vec3(-3, 4, -3.1)).look_at(Vec3(0, 0.5, 0)),
    Lighting(Vec3(0.2), [
        DirectedLight(Vec3(1, 0.8, -1.2), Vec3(250)),
    ], Vec3(175, 223, 241)),

    [   
        Body(
            Plane(Vec3(0, 0, 0)),
            Material(Vec3(230, 230, 230), 0, 1),
        ),

        Body(
            Box(Vec3(-0.5, 0, -0.5), Vec3(1)),
            Material(Vec3(40, 90, 215), 0, 1),
        ),

        Body(
            Box(Vec3(-0.1, 1, -0.35), Vec3(0.3)).rotate_pitch(25),
            Material(Vec3(215, 128, 40), 0, 1),
        ),
    ],
)


renderer = Renderer()
image_data = renderer.render(scene, 320, 160, filter=gamma_correction)

converter = PNGConverter()
converter.convert(image_data, "./res.png")

print("Rendered and saved")