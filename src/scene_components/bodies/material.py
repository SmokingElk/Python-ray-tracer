from math_tools.vectors import Vec3
from renderer.ray_model import RayModel

class Material:
    """Determines the interaction of light with an object."""
    def __init__(self, albedo: Vec3, glossiness: float, roughness: float):
        pass

    def _shader(self, collide: Vec3, ambient: Vec3, light_sources: list, ray_model: RayModel) -> tuple:
        """Determines the amount of light that will be reflected by the object."""