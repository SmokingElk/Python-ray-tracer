from src.scene_components.bodies.shapes.csg_shape_base import CSGShapeBase
from src.scene_components.bodies.shapes.shape_base import ShapeBase
from src.math_tools.vectors import Vec3
from src.scene_components.bodies.shapes.segments_operations import segments_union, segments_intersection, segments_difference



class Union(CSGShapeBase):
    """Union CSG operation."""
    def __init__(shape_a: ShapeBase, shape_b: ShapeBase):
        super().__init__(shape_a, shape_b)

    def _collider(ro: Vec3, rd: Vec3) -> list:
        pass


class Intersection(CSGShapeBase):
    """Intersection CSG operation."""
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        super().__init__(shape_a, shape_b)

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass


class Difference(CSGShapeBase):
    """Difference CSG operation."""
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        super().__init__(shape_a, shape_b)

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        pass
