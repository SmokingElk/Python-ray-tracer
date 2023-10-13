from math_tools.vectors import Vec3


class ShapeBase:
    def __init__(self):
        pass

    def translate(self, displacement: Vec3):
        """Performs a parallel transfer of the shape to the displacement vector."""

    def rotate_yaw(self, angle: float):
        """Shape's rotation in the plane YZ (in radians)"""
        
    def rotate_roll(self, angle: float):
        """Shape's rotation in the plane XY (in radians)"""

    def rotate_pitch(self, angle: float):
        """Shape's rotation in the plane XZ (in radians)"""

    def _transform(self, ro: Vec3, rd: Vec3) -> tuple:
        """Performs transformations over the beam, to implement shape transformations."""

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        """Calculates the segments of the intersection of a shape with a given ray. Redefined for each shape."""

    def _get_collide(self, ro: Vec3, rd: Vec3) -> list:
        """Returns the segments of the intersection of the shape with the specified ray, taking into account the transformations of the shape."""