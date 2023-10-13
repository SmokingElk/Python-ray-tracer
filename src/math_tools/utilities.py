from math import pi


def limit(value, minVal, maxVal):
    return min(maxVal, max(minVal, value))


def in_rad(degrees: float) -> float:
    return degrees / 180.0 * pi