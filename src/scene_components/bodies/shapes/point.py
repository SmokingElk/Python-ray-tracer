from math.vectors import Vec3
from bodies.shapes.shape_base import ShapeBase


class Point:
    """specifies a data structure that stores the position of a point on a numeric line, 
    the parent shape, and the normal at that point.
    """

    def __init__(self, value: float, parent_shape: ShapeBase, normal: Vec3):
       pass

    def reverse_normal(self):
        """Returns the normal's direction in the point. Used by CSG system."""

    def __eq__(self, other: "Point"):
        pass

    def __ne__(self, other: "Point"):
        pass

    def __lt__(self, other: "Point"):
        pass

    def __le__(self, other: "Point"):
        pass

    def __gt__(self, other: "Point"):
        pass

    def __ge__(self, other: "Point"):
        pass