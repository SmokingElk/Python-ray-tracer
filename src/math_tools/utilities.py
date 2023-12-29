from math import pi


def limit(value, minVal, maxVal):
    return min(maxVal, max(minVal, value))


def in_rad(degrees: float) -> float:
    return degrees / 180.0 * pi


def sign(value: float):
    return 1 if value >= 0 else -1
