from src.math_tools.vectors import Vec3
from src.scene_components.bodies.shapes.shape_base import ShapeBase


def min_point(*points):
    res = points[0]

    for i in points[1:]:
        if i < res:
            res = i

    return res


def max_point(*points):
    res = points[0]

    for i in points[1:]:
        if i > res:
            res = i

    return res


class Point:
    """specifies a data structure that stores the position of a point on a numeric line, 
    the parent shape, and the normal at that point.
    """

    def __init__(self, value: float, parent_shape: ShapeBase, normal: Vec3):
       self._value = value
       self._parent_shape = parent_shape
       self._normal = normal
       self._normDir = 1

    def reverse_normal(self):
        """Returns the normal's direction in the point. Used by CSG system."""
        self._normDir *= -1

    def get_normal(self):
        return self._normal * self._normDir

    def __eq__(self, other: "Point"):
        return self._value == other._value

    def __ne__(self, other: "Point"):
        return not (self == other)

    def __lt__(self, other: "Point"):
        return self._value < other._value

    def __le__(self, other: "Point"):
        return (self < other) or (self == other)

    def __gt__(self, other: "Point"):
        return not (self <= other)

    def __ge__(self, other: "Point"):
        return not (self < other)