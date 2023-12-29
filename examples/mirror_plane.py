import sys
import os
sys.path.append(os.getcwd())

from src.engine import (
    Vec3,
    Renderer,
    PNGConverter,
    PerspectiveCamera,
    Scene, Lighting, Body, Material,
    Sphere, Plane,
    DirectedLight, PointLight,
    gamma_correction,
)

scene = Scene(
    PerspectiveCamera(Vec3(0, 0, 0)),
    Lighting(Vec3(0.1), [
        PointLight(Vec3(0, 2.5, 4), Vec3(250, 250, 250)),
    ], Vec3(0, 0, 3)),

    [   
        Body(
            Plane(Vec3(0, -0.5, 0)),
            Material(Vec3(220, 220, 220), 0, 0.6),
        ),

        Body(
            Sphere(Vec3(-1, 0, 5), 0.5),
            Material(Vec3(232, 19, 19), 0, 1),
        ),

        Body(
            Sphere(Vec3(1, 0, 5), 0.5),
            Material(Vec3(19, 69, 232), 0, 1),
        ),
    ],
)


renderer = Renderer()
image_data = renderer.render(scene, 320, 160, filter=gamma_correction)

converter = PNGConverter()
converter.convert(image_data, "./res.png")

print("Rendered and saved")