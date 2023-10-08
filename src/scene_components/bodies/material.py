from math.vectors import Vec3


class Material:
    """Determines the interaction of light with an object."""
    def __init__(self, albedo: Vec3, glossiness: float, roughness: float):
        pass

    def _shader(self, ambient: Vec3, light_sources: list, in_shadow: function, reflected: Vec3) -> Vec3:
        """Determines the amount of light that will be reflected by the object."""