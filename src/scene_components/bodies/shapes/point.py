from math.vectors import Vec3
from bodies.shapes.shape_base import ShapeBase


class Point:
    """specifies a data structure that stores the position of a point on a numeric line, 
    the parent shape, and the normal at that point.
    """

    def __init__(value: float, parent_shape: ShapeBase, normal: Vec3):
       pass

    def reverse_normal():
        """Returns the normal's direction in the point. Used by CSG system."""

    def __eq__(other: "Point"):
        pass

    def __ne__(other: "Point"):
        pass

    def __lt__(other: "Point"):
        pass

    def __le__(other: "Point"):
        pass

    def __gt__(other: "Point"):
        pass

    def __ge__(other: "Point"):
        pass