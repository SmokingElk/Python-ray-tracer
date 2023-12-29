from src.math_tools.vectors import Vec3


class Lighting:
    """Sets the data structure describing the lighting of the scene."""

    def __init__(
        self, ambient: Vec3, light_sources: list, sky: Vec3, bounce_limit: int = 4
    ):
        self.ambient = ambient
        self.light_sources = light_sources
        self.sky = sky / 255.0
        self.bounce_limit = bounce_limit
