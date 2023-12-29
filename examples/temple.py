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
    PerspectiveCamera(Vec3(0, 1.5, -5), -15),
    Lighting(Vec3(0.2), [
        DirectedLight(Vec3(0.5, 0.5, -0.5), Vec3(250, 250, 250)),
    ], Vec3(175, 223, 241)),

    [   
        Body(
            Box(Vec3(-5, -1, -5), Vec3(10, 1, 10)),
            Material(Vec3(220, 220, 210), 0, 0.5),
        ),

        Body(
            Sphere(Vec3(0, 0.7, 0), 0.6),
            Material(Vec3(30, 30, 32), 0.6, 1),
        ),

        Body(
            Cylinder(Vec3(-3, 0, 3), 0.5),
            Material(Vec3(220, 220, 210), 0.5, 1),
        ),

        Body(
            ClampedCylinder(Vec3(-3, 0, 3), 0.6, 0.1),
            Material(Vec3(220, 220, 210), 0.5, 1),
        ),

        Body(
            Cylinder(Vec3(3, 0, 3), 0.5),
            Material(Vec3(220, 220, 210), 0.5, 1),
        ),

        Body(
            ClampedCylinder(Vec3(3, 0, 3), 0.6, 0.1),
            Material(Vec3(220, 220, 210), 0.5, 1),
        ),

        Body(
            ClampedCylinder(Vec3(0, 0, 0), 0.8, 0.1),
            Material(Vec3(220, 220, 210), 0.5, 1),
        ),
    ],
)


renderer = Renderer()
image_data = renderer.render(scene, 320, 160, filter=gamma_correction)

converter = PNGConverter()
converter.convert(image_data, "./res.png")

print("Rendered and saved")