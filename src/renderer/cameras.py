from renderer.camera_base import CameraBase


class OrthogonalCamera(CameraBase):
    """Realize an orthogonal projection."""
    def viewport(self, x: int, y: int, width: int, height: int) -> tuple:
        pass


class PerspectiveCamera(CameraBase):
    """Realize an perspective projection."""
    def viewport(self, x: int, y: int, width: int, height: int) -> tuple:
        pass