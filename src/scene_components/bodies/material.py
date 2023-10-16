from math_tools.vectors import Vec3


class Material:
    """Determines the interaction of light with an object."""
    def __init__(self, albedo: Vec3, glossiness: float, roughness: float):
        pass

    def _shader(self, collide: Vec3, ambient: Vec3, light_sources: list, in_shadow: function) -> Vec3:
        """Determines the amount of light that will be reflected by the object."""