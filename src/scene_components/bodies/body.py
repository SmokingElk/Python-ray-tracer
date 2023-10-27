from src.scene_components.bodies.shapes.shape_base import ShapeBase
from src.scene_components.bodies.material import Material
from src.math_tools.vectors import Vec3
from renderer.ray_model import RayModel


class Body:
    """sets the data structure that defines the scene object as a combination of form and material."""
    def __init__(self, shape: ShapeBase, material: Material):
        self.shape = shape
        self.material = material

    def get_collide(self, ro: Vec3, rd: Vec3) -> list:
        return self.shape._get_collide(ro, rd)
    
    def shader(self, collide: Vec3, ambient: Vec3, light_sources: list, ray_model: RayModel) -> tuple:
        return self.material._shader(
            collide,
            ambient,
            light_sources,
            ray_model   
        )