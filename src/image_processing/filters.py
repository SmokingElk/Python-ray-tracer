from src.math_tools.vectors import Vec3


def gamma_correction(color: Vec3) -> Vec3:
    return Vec3(
        color.x**0.45,
        color.y**0.45,
        color.z**0.45,
    )
