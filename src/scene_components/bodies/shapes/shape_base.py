from math_tools.vectors import Vec3
from math_tools.utilities import in_rad


class ShapeBase:
    def __init__(self):
        self._translate_vec = Vec3(0)

        self._yaw_angle = 0
        self._roll_angle = 0
        self._pitch_angle = 0

    def translate(self, displacement: Vec3):
        """Performs a parallel transfer of the shape to the displacement vector."""
        self._translate_vec += displacement

    def rotate_yaw(self, angle: float):
        """Shape's rotation in the plane YZ (in radians)"""
        self._yaw_angle -= in_rad(angle)

    def rotate_roll(self, angle: float):
        """Shape's rotation in the plane XY (in radians)"""
        self._roll_angle -= in_rad(angle)

    def rotate_pitch(self, angle: float):
        """Shape's rotation in the plane XZ (in radians)"""
        self._pitch_angle -= in_rad(angle)

    def _transform(self, ro: Vec3, rd: Vec3) -> tuple:
        """Performs transformations over the beam, to implement shape transformations."""
        roTranslated = ro - self._translate_vec
        roTransformed = roTranslated.rotateXZ(-self._pitch_angle).rotateYZ(-self._yaw_angle).rotateXY(-self._roll_angle)
        rdTransformed = rd.copy().rotateXZ(-self._pitch_angle).rotateYZ(-self._yaw_angle).rotateXY(-self._roll_angle)

        return roTransformed, rdTransformed

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        """Calculates the segments of the intersection of a shape with a given ray. Redefined for each shape."""

    def _get_collide(self, ro: Vec3, rd: Vec3) -> list:
        """Returns the segments of the intersection of the shape with the specified ray, taking into account the transformations of the shape."""
        roTransformed, rdTransformed = self._transform(ro, rd)
        return self._collider(roTransformed, rdTransformed)