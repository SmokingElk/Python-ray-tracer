from src.math_tools.vectors import Vec3
from src.scene_components.bodies.shapes.point import Point
from src.scene_components.lights.lighting import Lighting
from src.renderer.optic import reflect

NEAR_PLANE = 0.00000001
FAR_PLANE = 100


class RayModel:
    """simulates the movement of a light beam across the scene."""

    def __init__(self, lighting: Lighting, scene_objects: list):
        self.lighting = lighting
        self.scene_objects = scene_objects

    def _closest_collide(self, ro: Vec3, rd: Vec3) -> tuple:
        """determines the distance to the nearest intersection point of the specified ray with the objects of the scene,
        as well as the object with which this movement occurred."""

        closest = None
        closest_point = Point(FAR_PLANE, None, None)

        near_point = Point(NEAR_PLANE, None, None)
        far_point = Point(FAR_PLANE, None, None)

        for i in self.scene_objects:
            collide_points = i.get_collide(ro, rd)

            if len(collide_points) == 0 or collide_points[0] >= closest_point:
                continue

            for j in collide_points:
                if near_point < j < far_point and j < closest_point:
                    closest_point = j
                    closest = i
                    break

        return closest, closest_point

    def in_shadow_to_dir(self, point: Vec3, dir: Vec3) -> bool:
        """Checks if there any objects in given direction."""
        near_point = Point(NEAR_PLANE, None, None)
        far_point = Point(FAR_PLANE, None, None)

        for i in self.scene_objects:
            collide_points = i.get_collide(point, dir)

            if len(collide_points) == 0:
                continue

            for j in collide_points:
                if near_point < j < far_point:
                    return True

        return False

    def in_shadow_to_point(self, point: Vec3, point_to: Vec3) -> bool:
        """Checks if there any objects between to given points."""

        dir = (point_to - point).norm()
        closest_point = Point(FAR_PLANE, None, None)

        near_point = Point(NEAR_PLANE, None, None)
        far_point = Point(FAR_PLANE, None, None)

        for i in self.scene_objects:
            collide_points = i.get_collide(point, dir)

            if len(collide_points) == 0 or collide_points[0] >= closest_point:
                continue

            for j in collide_points:
                if near_point < j < far_point and j < closest_point:
                    closest_point = j
                    break

        return closest_point._value < (point_to - point).mag()

    def _cast_ray(self, ro: Vec3, rd: Vec3) -> tuple:
        """Calculates the illumination of the point where the specified beam hits."""
        closest, closest_point = self._closest_collide(ro.copy(), rd.copy())

        if closest == None:
            return Vec3(0), Vec3(0), self.lighting.sky, 1

        collide_point = ro + rd * closest_point._value
        normal = closest_point.get_normal()
        ray_reflected = reflect(rd, normal)

        color, roughness = closest.shader(
            collide_point,
            normal,
            ray_reflected,
            self.lighting.ambient,
            self.lighting.light_sources,
            self,
        )

        return collide_point, ray_reflected, color, roughness

    def trace_ray(self, ro: Vec3, rd: Vec3) -> Vec3:
        """determines the amount of light received from the direction opposite to rd by the point ro (reverse ray tracing)."""
        res = Vec3(0, 0, 0)

        objectColors = []
        objectRoughness = []

        for i in range(self.lighting.bounce_limit):
            collide_point, ray_reflected, color, roughness = self._cast_ray(ro, rd)

            objectColors.append(color)
            objectRoughness.append(roughness)

            if roughness == 1:
                break

            ro = collide_point
            rd = ray_reflected

        if len(objectColors) == 0:
            return res

        res = objectColors[-1]

        for i in range(len(objectColors) - 2, -1, -1):
            res = res * (1 - objectRoughness[i]) + objectColors[i] * objectRoughness[i]

        return res
