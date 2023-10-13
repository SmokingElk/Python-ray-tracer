from bodies.shapes.csg_shape_base import CSGShapeBase
from bodies.shapes.shape_base import ShapeBase
from math_tools.vectors import Vec3


class Union(CSGShapeBase):
    """Union CSG operation."""
    def __init__(shape_a: ShapeBase, shape_b: ShapeBase):
        pass

    def _collider(ro: Vec3, rd: Vec3) -> list:
        pass


class Intersection(CSGShapeBase):
    """Intersection CSG operation."""
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        pass

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass


class Difference(CSGShapeBase):
    """Difference CSG operation."""
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        pass

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass
