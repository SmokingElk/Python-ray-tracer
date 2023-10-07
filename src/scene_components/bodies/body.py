from bodies.shapes.shape_base import ShapeBase
from bodies.material import Material


class Body:
    """sets the data structure that defines the scene object as a combination of form and material."""
    def __init__(shape: ShapeBase, material: Material):
        pass