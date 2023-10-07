from math.vectors import Vec3


class LightSourceBase:
    """sets the data structure describing the light source"""
    def __init__(color: Vec3):
        pass
    
    def get_dir(dot: Vec3) -> Vec3:
        """Returns the vector directed from the point to the light source."""