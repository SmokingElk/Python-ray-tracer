from src.math_tools.vectors import Vec3


def reflect(source_dir: Vec3, normal: Vec3) -> Vec3:
    """Calculates a reflected direction of source_dir."""
    return source_dir - (normal * 2 * (normal @ source_dir))
