from bodies.shapes.shape_base import ShapeBase
from math.vectors import Vec3


class Box(ShapeBase):
    def __init__(self, pos: Vec3, size: Vec3):
        pass

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass


class Sphere(ShapeBase): 
    def __init__(self, pos: Vec3, radius: float):
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
