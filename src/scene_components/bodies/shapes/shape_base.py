from math.vectors import Vec3


class ShapeBase:
    def __init__():
        pass

    def translate(displacement: Vec3):
        """Performs a parallel transfer of the shape to the displacement vector."""

    def rotate_yaw(angle: float):
        """Shape's rotation in the plane YZ (in radians)"""
        
    def rotate_roll(angle: float):
        """Shape's rotation in the plane XY (in radians)"""

    def rotate_pitch(angle: float):
        """Shape's rotation in the plane XZ (in radians)"""

    def _transform(ro: Vec3, rd: Vec3) -> tuple:
        """Performs transformations over the beam, to implement shape transformations."""

    def _collider(ro: Vec3, rd: Vec3) -> list:
        """Calculates the segments of the intersection of a shape with a given ray. Redefined for each shape."""

    def _get_collide(ro: Vec3, rd: Vec3) -> list:
        """Returns the segments of the intersection of the shape with the specified ray, taking into account the transformations of the shape."""