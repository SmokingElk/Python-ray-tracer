from src.math_tools.vectors import Vec3
from src.math_tools.utilities import in_rad
from math import atan2, asin


class CameraBase:
    def __init__(
        self, pos: Vec3, yaw: float, roll: float, pitch: float, FOV: float = 60
    ):
        """
        pos - camera position
        yaw - camera rotation in the plane YZ (in radians)
        roll - camera rotation in the plane XY (in radians)
        pitch - camera rotation in the plane XZ (in radians)"""

        self._pos = pos
        self._yaw = in_rad(yaw)
        self._roll = -in_rad(roll)
        self._pitch = -in_rad(pitch)
        self._FOV = in_rad(FOV)

    def look_at(self, look_point: Vec3):
        """Rotates the camera such a way the frames center will be looking in look_point."""
        dir_to_look = (look_point - self._pos).norm()

        self._roll = -atan2(dir_to_look.x, dir_to_look.z)
        self._yaw = -asin(dir_to_look.y)

    def viewport(
        self, x: int, y: int, width: int, height: int, pixel_aspect: float
    ) -> tuple:
        """Transform pixel coordinates to the ray's intersecting it origine and direction."""
