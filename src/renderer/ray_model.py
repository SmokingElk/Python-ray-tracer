from math.vectors import Vec3
from scene_components.scene import Scene
from scene_components.lights.light_source_base import LightSourceBase

class RayModel:
    """simulates the movement of a light beam across the scene."""
    def __init__(lighting: dict, scene_objects: list):
        pass

    def _closest_collide(ro: Vec3, rd: Vec3) -> tuple:
        """determines the distance to the nearest intersection point of the specified ray with the objects of the scene, 
        as well as the object with which this movement occurred."""
    
    def _in_shadow(dot: Vec3, light_source: LightSourceBase) -> bool:
        """Checks if the dot is in shadow, relative to the specified light source."""
    
    def _cast_ray(ro: Vec3, rd: Vec3) -> Vec3: 
        """Calculates the illumination of the point where the specified beam hits."""
    
    def trace_ray(ro: Vec3, rd: Vec3) -> Vec3: 
        """determines the amount of light received from the direction opposite to rd by the point ro (reverse ray tracing)."""

