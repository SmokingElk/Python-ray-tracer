from scene_components.lights.lighting import Lighting
from renderer.camera_base import CameraBase


class Scene:
    """specifies a data structure that stores all the parameters of the scene to be rendered, such as: 
    camera parameters, lighting parameters and a list of scene objects."""
    def __init__(self, camera: CameraBase, lighting: Lighting, scene_objects: list):
        pass