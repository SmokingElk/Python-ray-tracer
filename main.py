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
    PerspectiveCamera(Vec3(0, 0.9, -2.9)).look_at(Vec3(0, 0.7, 0)),
    Lighting(Vec3(0.2), [
        PointLight(Vec3(0, 2, 0), Vec3(250)),
    ], Vec3(175, 223, 241), bounce_limit=100),

    [   
        Body(
            Plane(Vec3(-2, 0, -3), Vec3(1, 0, 0)),
            Material(Vec3(220), 0, 0.3),
        ),

        Body(
            Plane(Vec3(-3, 0, -3), Vec3(0, 1, 0)),
            Material(Vec3(220)),
        ),

        Body(
            Plane(Vec3(-3, 0, -3), Vec3(0, 0, 1)),
            Material(Vec3(220), 0, 0.3),
        ),

        Body(
            Plane(Vec3(2, 6, 3), Vec3(-1, 0, 0)),
            Material(Vec3(220), 0, 0.3),
        ),

        Body(
            Plane(Vec3(3, 4, 3), Vec3(0, -1, 0)),
            Material(Vec3(220)),
        ),

        Body(
            Plane(Vec3(3, 6, 3), Vec3(0, 0, -1)),
            Material(Vec3(220), 0, 0.3),
        ),

        Body(
            Sphere(Vec3(0, 0.6, 0.5), 0.6),
            Material(Vec3(30, 100, 220)),
        ),
    ],
)


renderer = Renderer()
image_data = renderer.render(scene, 320, 160, filter=gamma_correction)

converter = PNGConverter()
converter.convert(image_data, "./res.png")
