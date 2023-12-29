from src.math_tools.vectors import Vec3
from src.renderer.ray_model import RayModel

GLARE_SIZE = 64


class Material:
    """Determines the interaction of light with an object."""

    def __init__(self, albedo: Vec3, glossiness: float = 0, roughness: float = 1):
        self._albedo = albedo / 255.0
        self._gloiness = glossiness
        self._roughness = roughness

    def _shader(
        self,
        collide: Vec3,
        normal: Vec3,
        reflected: Vec3,
        ambient: Vec3,
        light_sources: list,
        ray_model: RayModel,
    ) -> tuple:
        """Determines the amount of light that will be reflected by the object."""
        diffuse_integral = Vec3(0)
        specular_integral = Vec3(0)

        for i in light_sources:
            if i.in_shadow(collide, ray_model):
                continue

            to_light = i.get_dir(collide)

            diffuse_light_density = max(0, to_light @ normal)
            diffuse_integral += i.color * diffuse_light_density

            specular_light_density = max(0, to_light @ reflected) ** GLARE_SIZE
            specular_integral += i.color * specular_light_density

        diffuse_integral /= len(light_sources)
        specular_integral /= len(light_sources)

        light_full = ambient + Vec3(1 - ambient.x, 1 - ambient.y, 1 - ambient.z) * (
            diffuse_integral * (1 - self._gloiness) + specular_integral * self._gloiness
        )

        return self._albedo * light_full, self._roughness
