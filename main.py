from src.engine import (
    Vec3,
    Renderer,
    PNGConverter, UnicodeConverter,
    PerspectiveCamera,
    Scene, Lighting, Body, Material,
    Sphere, Plane, Box, Cylinder, ClampedCylinder,
    DirectedLight, PointLight,
    Union, Intersection, Difference,
    gamma_correction,
)

scene = Scene(
    PerspectiveCamera(Vec3(0, 0.5, -5)),
    Lighting(Vec3(0.2), [
        DirectedLight(Vec3(1, 1, -1), Vec3(250)),
    ], Vec3(232,239,241)),

    [   
        Body(
            Plane(Vec3(0, 0, 0)),
            Material(Vec3(220), 0, 0.5),
        ),

        Body(
            Sphere(Vec3(0, 0.6, 0), 0.6),
            Material(Vec3(30, 100, 220)),
        ),
    ],
)


renderer = Renderer()
image_data = renderer.render(scene, 80, 80 / 24 * 11, 11 / 24)

converter = UnicodeConverter(" .:!r(lH@"[::-1])
print(converter.convert(image_data))
