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
    Union, Intersection, Difference,
    gamma_correction,
)

scene = Scene(
    PerspectiveCamera(Vec3(0.75, 0.9, -3.1)).look_at(Vec3(0.6, 0.5, 0)),
    Lighting(Vec3(0.2), [
        DirectedLight(Vec3(1, 0.8, -1.2), Vec3(250)),
    ], Vec3(175, 223, 241)),

    [   
        Body(
            Plane(Vec3(0, 0, 0)),
            Material(Vec3(230, 230, 230), 0, 1),
        ),

        Body(
            Difference(
                Box(Vec3(-0.5, 0, -0.5), Vec3(1)),
                Union(
                    Cylinder(Vec3(0, 0.6, 0), 0.2).rotate_yaw(90),
                    Box(Vec3(-0.2, 0, -2), Vec3(0.4, 0.6, 4)),
                ),
            ),
            
            Material(Vec3(40, 90, 215), 0, 1),
        ),

        Body(
            Intersection(
                Box(Vec3(1.5 - 0.3, 0, -0.3), Vec3(0.6)),
                Sphere(Vec3(1.5, 0.3, 0), 0.4),
            ),

            Material(Vec3(215, 128, 40), 0, 1),
        )
    ],
)


renderer = Renderer()
image_data = renderer.render(scene, 320, 160, filter=gamma_correction)

converter = PNGConverter()
converter.convert(image_data, "./res.png")

print("Rendered and saved")