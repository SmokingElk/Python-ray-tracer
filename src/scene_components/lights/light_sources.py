from src.math_tools.vectors import Vec3
from src.scene_components.lights.light_source_base import LightSourceBase
from src.renderer.ray_model import RayModel


class PointLight(LightSourceBase):
    """Specifies a data structure describing a point light source."""
    def __init__(self, pos: Vec3, color: Vec3):
        super().__init__(color)
        self.pos = pos.copy()

    def get_dir(self, point: Vec3) -> Vec3:
        return (self.pos - point).norm()

    def in_shadow(self, point: Vec3, ray_model: RayModel) -> bool:
        return ray_model.in_shadow_to_point(point, self.pos)


class DirectedLight(LightSourceBase):
    """Specifies a data structure describing a directed light source."""
    def __init__(self, dir: Vec3, color: Vec3):
        super().__init__(color)
        self.dir = dir.copy().norm()

    def get_dir(self, point: Vec3) -> Vec3:
        return self.dir.copy()
    
    def in_shadow(self, point: Vec3, ray_model: RayModel) -> bool:
        return ray_model.in_shadow_to_dir(point, self.dir)