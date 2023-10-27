from src.renderer.camera_base import CameraBase
from src.math_tools.vectors import Vec3
from math import tan


class OrthogonalCamera(CameraBase):
    """Realize an orthogonal projection."""
    def __init__(self, pos: Vec3, yaw: float, roll: float, pitch: float):
        super().__init__(self, pos, yaw, roll, pitch)

    def viewport(self, x: int, y: int, width: int, height: int) -> tuple:
        aspect_ratio = width / height

        offsetX = (x / width - 0.5) * aspect_ratio
        offsetY = (height - y) / height - 0.5
        offsetZ = 0

        offset = Vec3(offsetX, offsetY, offsetZ).norm()

        offset.rotateXY(self._roll)
        offset.rotateYZ(self._yaw)
        offset.rotateXZ(self._pitch)

        ro = self._pos + offset

        rd = Vec3(0, 0, 1)
        
        rd.rotateXY(self._roll)
        rd.rotateYZ(self._yaw)
        rd.rotateXZ(self._pitch)

        return ro, rd


class PerspectiveCamera(CameraBase):
    """Realize an perspective projection."""
    def __init__(self, pos: Vec3, yaw: float=0.0, roll: float=0.0, pitch: float=0.0):
        super().__init__(self, pos, yaw, roll, pitch)

    def viewport(self, x: int, y: int, width: int, height: int) -> tuple:
        aspect_ratio = width / height

        rdX = (x / width - 0.5) * aspect_ratio
        rdY = (height - y) / height - 0.5
        rdZ = aspect_ratio / 2 / tan(self._FOV / 2)

        ro = self._pos.copy()
        rd = Vec3(rdX, rdY, rdZ).norm()

        rd.rotateXY(self._roll)
        rd.rotateYZ(self._yaw)
        rd.rotateXZ(self._pitch)

        return ro, rd
