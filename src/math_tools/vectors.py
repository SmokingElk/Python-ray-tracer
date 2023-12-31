from math import cos, sin


def lerp(a: float, b: float, mixing: float) -> float:
    return a + (b - a) * mixing


class Vec3:
    def __init__(self, x, y=None, z=None):
        self.x = x
        self.y = self.x if y == None else y
        self.z = self.y if z == None else z

    def __add__(self, other: "Vec3"):
        """Returns vectors sum."""
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __iadd__(self, other: "Vec3"):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other: "Vec3"):
        """Returns vectors difference."""
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __isub__(self, other: "Vec3"):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other: "Vec3"):
        "Returns product of the vector and a number or another vector."
        if not isinstance(other, Vec3):
            return Vec3(
                self.x * other,
                self.y * other,
                self.z * other,
            )

        return Vec3(
            self.x * other.x,
            self.y * other.y,
            self.z * other.z,
        )

    def __imul__(self, other: "Vec3"):
        if not isinstance(other, Vec3):
            self.x *= other
            self.y *= other
            self.z *= other
            return self

        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self

    def __truediv__(self, other: "Vec3"):
        """Returns product of the vector and an inverse number or another vector."""
        if not isinstance(other, Vec3):
            return Vec3(
                self.x / other,
                self.y / other,
                self.z / other,
            )

        return Vec3(
            self.x / other.x,
            self.y / other.y,
            self.z / other.z,
        )

    def __itruediv__(self, other: "Vec3"):
        if not isinstance(other, Vec3):
            self.x /= other
            self.y /= other
            self.z /= other
            return self

        self.x /= other.x
        self.y /= other.y
        self.z /= other.z
        return self

    def __matmul__(self, other: "Vec3"):
        """Returns dot product of 2 vectors."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def rotateXY(self, angle: float):
        "Rotates the vector in the plane XY"
        x = self.x
        y = self.y

        self.x = x * cos(angle) - y * sin(angle)
        self.y = x * sin(angle) + y * cos(angle)

        return self

    def rotateXZ(self, angle: float):
        "Rotates the vector in the plane XY"
        x = self.x
        z = self.z

        self.x = x * cos(angle) - z * sin(angle)
        self.z = x * sin(angle) + z * cos(angle)

        return self

    def rotateYZ(self, angle: float):
        "Rotates the vector in the plane YZ"
        z = self.z
        y = self.y

        self.z = z * cos(angle) - y * sin(angle)
        self.y = z * sin(angle) + y * cos(angle)

        return self

    def mag(self):
        """Returns vector's magnitude."""
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def norm(self):
        """Makes vector's length equals 1."""
        self /= self.mag()
        return self

    def mix(self, other: "Vec3", mixing: float):
        """Returns a linear interpolation of 2 vectors."""
        return Vec3(
            lerp(self.x, other.x, mixing),
            lerp(self.y, other.y, mixing),
            lerp(self.z, other.z, mixing),
        )

    def __str__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"

    def copy(self):
        """Returns a vector's copy."""
        return Vec3(self.x, self.y, self.z)
