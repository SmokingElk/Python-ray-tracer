from math_tools.vectors import Vec3
from scene_components.scene import Scene
from scene_components.lights.light_source_base import LightSourceBase
from scene_components.bodies.shapes.point import Point
from renderer.optic import reflect

NEAR_PLANE = 0.000000000001
FAR_PLANE = 100


class RayModel:
    """simulates the movement of a light beam across the scene."""
    def __init__(self, lighting: dict, scene_objects: list):
        self.lighting = lighting
        self.scene_objects = scene_objects

    def _closest_collide(self, ro: Vec3, rd: Vec3, near_plane: float, far_plane: float) -> tuple:
        """determines the distance to the nearest intersection point of the specified ray with the objects of the scene, 
        as well as the object with which this movement occurred."""

        closest = None
        closest_point = Point(far_plane, None, None)

        near_point = Point(near_plane, None, None)
        far_point = Point(far_plane, None, None)

        for i in self.scene_objects:
            collide_points = i._get_collide(ro, rd)

            if len(collide_points) == 0 or collide_points[0] >= closest_point:
                continue

            for j in collide_points:
                if near_point < j < far_point and j < closest_point:
                    closest_point = j
                    closest = i
                    break

        return closest, closest_point
    
    def _in_shadow(self, dot: Vec3, light_source: LightSourceBase) -> bool:
        """Checks if the dot is in shadow, relative to the specified light source."""
    
    def _cast_ray(self, ro: Vec3, rd: Vec3) -> tuple: 
        """Calculates the illumination of the point where the specified beam hits."""
        closest, closest_point = self._closest_collide(ro, rd, NEAR_PLANE, FAR_PLANE)

        if closest == None:
            return Vec3(0), Vec3(0), self.lighting.sky, 0

        collide_point = ro + rd * closest_point._value
        normal = closest_point.get_normal()

        color, reflectance = closest.shader(
            collide_point, 
            normal,
            self.lighting.ambient, 
            self.lighting.light_source
        ) # ДОБАВИТЬ IN_SHADOW!
        
        return collide_point, normal, color, reflectance

    def trace_ray(self, ro: Vec3, rd: Vec3) -> Vec3: 
        """determines the amount of light received from the direction opposite to rd by the point ro (reverse ray tracing)."""
        res = Vec3(0, 0, 0)
        reflectance = 1

        for i in range(self.lighting.bounce_limit):
            collide_point, normal, color, next_reflectance = self._cast_ray(ro, rd)

            res = res * (1 - reflectance) + color * reflectance

            if next_reflectance == 0:
                break

            ro = collide_point
            rd = reflect(rd, normal)
            reflectance = next_reflectance

        return res

