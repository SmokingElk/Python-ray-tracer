from math.vectors import Vec3


class LightSourceBase:
    """sets the data structure describing the light source"""
    def __init__(self, color: Vec3):
        pass
    
    def get_dir(self, dot: Vec3) -> Vec3:
        """Returns the vector directed from the point to the light source."""