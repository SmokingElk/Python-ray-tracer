from src.scene_components.bodies.shapes.shape_base import ShapeBase
from src.math_tools.vectors import Vec3
from math import sqrt
from src.scene_components.bodies.shapes.point import Point, min_point, max_point


class Sphere(ShapeBase): 
    def __init__(self, pos: Vec3, radius: float):
        super().__init__()
        self.translate(pos)
        self.radius = radius
        self._radius2 = radius**2

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        a = rd @ rd
        b = ro @ rd
        c = (ro @ ro) - self._radius2

        D = b**2 - a * c

        if (D < 0): 
            return []

        sqrtD = sqrt(D)
        t1 = (-b + sqrtD) / a
        t2 = (-b - sqrtD) / a

        normal1 = (ro + rd * t1).norm()
        normal2 = (ro + rd * t2).norm()

        point1 = Point(t1, self, normal1)
        point2 = Point(t2, self, normal2)

        if t1 < t2:
            return [point1, point2]
        
        return [point2, point1]


class Box(ShapeBase):
    def __init__(self, pos: Vec3, size: Vec3):
        pass

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass


class Cylinder(ShapeBase):
    def __init__(self, pos: Vec3, radius: float):
        pass

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass


class ClampedCylinder(ShapeBase):
    def __init__(self, pos: Vec3, radius: float, height: float):
        pass

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass


class Plane(ShapeBase): 
    def __init__(self, pos: Vec3, normal: Vec3):
        pass

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass


class Disk(ShapeBase):
    def __init__(self, pos: Vec3, radius: float, normal: Vec3):
        pass
    
    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass
