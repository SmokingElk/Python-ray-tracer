from math_tools.vectors import Vec3
from renderer.ray_model import RayModel

class LightSourceBase:
    """sets the data structure describing the light source"""
    def __init__(self, color: Vec3):
        self.color = color / 255.0

    def get_dir(self, point: Vec3) -> Vec3:
        """Returns the vector directed from the point to the light source."""
    
    def in_shadow(self, point: Vec3, ray_model: RayModel) -> bool:
        """Checks if the light source in shadow."""