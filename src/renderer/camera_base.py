from math.vectors import Vec3


class CameraBase:
    def __init__(pos: Vec3, yaw: float, roll: float, pitch: float):
        """
        pos - camera position
        yaw - camera rotation in the plane YZ (in radians)
        roll - camera rotation in the plane XY (in radians)
        pitch - camera rotation in the plane XZ (in radians)"""

    def look_at(look_point: Vec3):
        """Rotates the camera such a way the frames center will be looking in look_point."""

    def viewport(x: int, y: int, width: int, height: int) -> tuple:
        """Transform pixel coordinates to the ray's intersecting it origine and direction."""