from bodies.shapes.shape_base import ShapeBase
from math_tools.vectors import Vec3


class CSGShapeBase(ShapeBase): 
    def __init__(self, shape_a: ShapeBase, shape_b: ShapeBase):
        """Takes 2 shapes-operands and realize a CSG operation."""
    
    def translate(self, displacement: Vec3):
        """Performs a parallel transfer of the operands to the displacement vector."""
    
    def rotate_yaw(self):
        """Shapes rotation isn't supported."""

    def rotate_roll(self):
        """Shapes rotation isn't supported."""
    
    def rotate_pitch(self):
        """Shapes rotation isn't supported."""