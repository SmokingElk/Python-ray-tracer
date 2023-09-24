def lerp(a, b, mixing):
    return a + (b - a) * mixing   


class Vec3:
    def __init__(self, x, y=None, z=None):
        self.x = x
        self.y = self.x if y == None else y 
        self.z = self.y if z == None else z

    def __add__(self, other):
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __sub__(self, other):
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def __mul__(self, other):
        if instance(other, Vec3):
            return Vec3(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z,
            )

        return Vec3(
            self.x * other,
            self.y * other,
            self.z * other,
        )

    def __imul__(self, other):
        if instance(other, Vec3): 
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
            return

        self.x *= other.x
        self.y *= other.y
        self.z *= other.z

    def __truediv__(self, other):
        if instance(other, Vec3):
            return Vec3(
                self.x / other.x,
                self.y / other.y,
                self.z / other.z,
            )

        return Vec3(
            self.x /other,
            self.y / other,
            self.z / other,
        )

    def __itruediv__(self, other):
        if instance(other, Vec3): 
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
            return

        self.x /= other.x
        self.y /= other.y
        self.z /= other.z

    def __len__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def norm(self):
        self /= len(self)
        return self

    def mix(self, other, mixing):
        return Vec3(
            lerp(self.x, other.x, mixing),
            lerp(self.y, other.y, mixing),
            lerp(self.z, other.z, mixing),
        )

    def __str__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"

    def copy(self):
        return Vec3(self.x, self.y, self.z)
