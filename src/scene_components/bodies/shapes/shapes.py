from src.scene_components.bodies.shapes.shape_base import ShapeBase
from src.math_tools.vectors import Vec3
from src.math_tools.utilities import sign
from math import sqrt
from src.scene_components.bodies.shapes.point import Point, min_point, max_point

EPS = 0.0000000001


class Sphere(ShapeBase): 
    def __init__(self, pos: Vec3, radius: float):
        super().__init__()
        self.translate(pos)
        self.radius = radius
        self._radius2 = radius**2

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        a = rd @ rd
        b = ro @ rd
        c = (ro @ ro) - self._radius2

        D = b**2 - a * c

        if (D < 0): 
            return []

        sqrtD = sqrt(D)
        t1 = (-b + sqrtD) / a
        t2 = (-b - sqrtD) / a

        normal1 = (ro + rd * t1).norm()
        normal2 = (ro + rd * t2).norm()

        point1 = Point(t1, self, normal1)
        point2 = Point(t2, self, normal2)

        if t1 < t2:
            return [point1, point2]
        
        return [point2, point1]


class Box(ShapeBase):
    def __init__(self, pos: Vec3, size: Vec3):
        super().__init__()
        self.translate(pos)

        self.sizeX = size.x
        self.sizeY = size.y
        self.sizeZ = size.z

    def collideXY(self, x, y):
        return 0 <= x <= self.sizeX and 0 <= y <= self.sizeY
    
    def collideXZ(self, x, z):
        return 0 <= x <= self.sizeX and 0 <= z <= self.sizeZ
    
    def collideYZ(self, y, z):
        return 0 <= z <= self.sizeZ and 0 <= y <= self.sizeY

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        points = []

        rdX = rd.x if abs(rd.x) > EPS else EPS
        rdY = rd.y if abs(rd.y) > EPS else EPS
        rdZ = rd.z if abs(rd.z) > EPS else EPS

        t = -ro.z / rdZ
        if self.collideXY(ro.x + rdX * t, ro.y + rdY * t):
            points.append(Point(t, self, Vec3(0, 0, -1)))
        
        t = (self.sizeZ - ro.z) / rdZ
        if self.collideXY(ro.x + rdX * t, ro.y + rdY * t):
            points.append(Point(t, self, Vec3(0, 0, 1)))

        t = -ro.y / rdY
        if self.collideXZ(ro.x + rdX * t, ro.z + rdZ * t):
            points.append(Point(t, self, Vec3(0, -1, 0)))

        t = (self.sizeY - ro.y) / rdY
        if self.collideXZ(ro.x + rdX * t, ro.z + rdZ * t):
            points.append(Point(t, self, Vec3(0, 1, 0)))
    
        t = -ro.x / rdX
        if self.collideYZ(ro.y + rdY * t, ro.z + rdZ * t):
            points.append(Point(t, self, Vec3(-1, 0, 0)))
    
        t = (self.sizeX - ro.x) / rdX
        if self.collideYZ(ro.y + rdY * t, ro.z + rdZ * t):
            points.append(Point(t, self, Vec3(1, 0, 0)))
        
        if len(points) < 2:
            return []

        return [min_point(*points), max_point(*points)]


class Cylinder(ShapeBase):
    def __init__(self, pos: Vec3, radius: float):
        super().__init__()
        self.translate(pos)
        self._radius2 = radius**2
        

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        o = Vec3(ro.x, 0, ro.z)
        d = Vec3(rd.x, 0, rd.z)

        a = d @ d
        b = o @ d
        c = (o @ o) - self._radius2

        D = b**2 - a * c
        if D < 0:
            return []
        sqrtD = sqrt(D)

        res1 = (-b + sqrtD) / a
        res2 = (-b - sqrtD) / a

        p1 = ro + rd * res1
        p2 = ro + rd * res2

        dot1 = Point(res1, self, Vec3(p1.x, 0, p1.z).norm())
        dot2 = Point(res2, self, Vec3(p2.x, 0, p2.z).norm())

        return [min_point(dot1, dot2), max_point(dot1, dot2)]


class ClampedCylinder(ShapeBase):
    def __init__(self, pos: Vec3, radius: float, height: float):
        super().__init__()
        self.translate(pos)
        self._radius2 = radius**2
        self._height = height

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        points = []

        rdY = rd.y if abs(rd.y) > EPS else EPS * sign(rd.y)

        bottom = -ro.y / rdY
        if (ro.x + rd.x * bottom)**2 + (ro.z + rd.z * bottom)**2 <= self._radius2:
            points.append(Point(bottom, self, Vec3(0, -1, 0)))

        top = (self._height - ro.y) / rdY
        if (ro.x + rd.x * top)**2 + (ro.z + rd.z * top)**2 <= self._radius2:
            points.append(Point(top, self, Vec3(0, 1, 0)))

        o = Vec3(ro.x, 0, ro.z)
        d = Vec3(rd.x, 0, rd.z)

        a = d @ d
        b = o @ d
        c = (o @ o) - self._radius2

        D = b**2 - a * c
        
        if D >= 0:
            sqrtD = sqrt(D)

            t1 = (-b + sqrtD) / a
            t2 = (-b - sqrtD) / a

            if bottom <= t1 <= top and rdY >= 0 or top <= t1 <= bottom and rdY < 0:
                p1 = ro + rd * t1
                points.append(Point(t1, self, Vec3(p1.x, 0, p1.z).norm()))

            if bottom <= t2 <= top and rdY >= 0 or top <= t2 <= bottom and rdY < 0:
                p2 = ro + rd * t2
                points.append(Point(t2, self, Vec3(p2.x, 0, p2.z).norm()))

        if len(points) < 2:
            return []

        return [min_point(*points), max_point(*points)]


class Plane(ShapeBase): 
    def __init__(self, pos: Vec3, normal: Vec3=Vec3(0, 1, 0)):
        super().__init__()
        self.translate(pos)
        self._norm = normal.copy().norm()

    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        rdN = (rd @ self._norm)
        res = float("inf") if rdN == 0 else -(ro @ self._norm) / (rd @ self._norm)
        return [Point(res, self, self._norm), Point(res, self, self._norm)]


class Disk(ShapeBase):
    def __init__(self, pos: Vec3, radius: float, normal: Vec3):
        super().__init__()
        self.translate(pos)
        self._norm = normal.copy().norm()
        self._radius2 = radius**2
    
    def _collider(self, ro: Vec3, rd: Vec3) -> list:
        rdN = (rd @ self._norm)
        res = float("inf") if rdN == 0 else -(ro @ self._norm) / (rd @ self._norm)

        p = ro + rd * res
        if p @ p > self._radius2:
            return []
        return [Point(res, self, self._norm), Point(res, self, self._norm)]
