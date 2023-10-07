from bodies.shapes.shape_base import ShapeBase
from math.vectors import Vec3


class CSGShapeBase(ShapeBase): 
    def __init__(shape_a: ShapeBase, shape_b: ShapeBase):
        """Takes 2 shapes-operands and realize a CSG operation."""
    
    def translate(displacement: Vec3):
        """Performs a parallel transfer of the operands to the displacement vector."""
    
    def rotate_yaw():
        """Shapes rotation isn't supported."""

    def rotate_roll():
        """Shapes rotation isn't supported."""
    
    def rotate_pitch():
        """Shapes rotation isn't supported."""