from src.scene_components.bodies.shapes.csg_shape_base import CSGShapeBase
from src.scene_components.bodies.shapes.shape_base import ShapeBase
from src.math_tools.vectors import Vec3
from src.scene_components.bodies.shapes.segments_operations import segments_union, segments_intersection, segments_difference


class Union(CSGShapeBase):
    """Union CSG operation."""
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        super().__init__(shape_a, shape_b)

    def _get_collide(self, ro: Vec3, rd: Vec3) -> list:
        lineA = self.shape_a._get_collide(ro, rd)
        lineB = self.shape_b._get_collide(ro, rd)
        return segments_union(lineA, lineB)


class Intersection(CSGShapeBase):
    """Intersection CSG operation."""
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        super().__init__(shape_a, shape_b)

    def _get_collide(self, ro: Vec3, rd: Vec3) -> list:
        lineA = self.shape_a._get_collide(ro, rd)
        lineB = self.shape_b._get_collide(ro, rd)
        return segments_intersection(lineA, lineB)


class Difference(CSGShapeBase):
    """Difference CSG operation."""
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        super().__init__(shape_a, shape_b)

    def _get_collide(self, ro: Vec3, rd: Vec3) -> list:
        lineA = self.shape_a._get_collide(ro, rd)
        lineB = self.shape_b._get_collide(ro, rd)
        return segments_difference(lineA, lineB)
