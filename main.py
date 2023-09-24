from vectors import Vec3


def main():
    a = Vec3(1, 2, 1)
    b = Vec3(3, 5, -6)
    c = a + b

    print(a, b, c)

    aCopy = a.copy()
    aCopy.x = 5
    print(a, aCopy)

    print(a.mag())

    aCopy.norm()
    print(aCopy.mag())

    bCopy = b.copy()
    print(b * 0.5)

    v1 = Vec3(1, 0.5, 1)
    v2 = Vec3(0.5, 0.5, 0)
    v1 *= v2
    print(v1)


if __name__ == "__main__":
    main()