from src.engine import (
    Vec3,
    Renderer,
    PNGConverter,
    PerspectiveCamera,
    Scene, Lighting, Body, Material,
    Sphere, Plane,
    DirectedLight,
    gamma_correction,
)

scene = Scene(
    PerspectiveCamera(Vec3(0, 0, 0), 0, 0, 0),
    Lighting(
        Vec3(0.2),
        [DirectedLight(Vec3(0.5, 0.5, -0.5), Vec3(250, 250, 250))],
        Vec3(91, 200, 241),
    ),
    [
        Body(
            Plane(Vec3(0, -0.5, 0)),
            Material(Vec3(220, 220, 220), 0, 1),
        ),

        Body(
            Sphere(Vec3(0, 0, 5), 0.5),
            Material(Vec3(19, 97, 232), 0, 1),
        ),
    ],
)

renderer = Renderer()
image_data = renderer.render(scene, 320, 160, filter=gamma_correction)

converter = PNGConverter()
converter.convert(image_data, "./res.png")

# image_data = renderer.render(scene, int(80 * 24 / 11), 45, 11 / 24)

# converter = UnicodeConverter(" .:!r(lH@")
# print(converter.convert(image_data))
