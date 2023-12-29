from src.scene_components.bodies.shapes.point import Point, min_point, max_point
from src.math_tools.vectors import Vec3


def get_seg(num_line, seg_num):
    return [num_line[2 * int(seg_num)], num_line[2 * int(seg_num) + 1]]


def segments_union(lineA, lineB):
    if len(lineA) == 0 and len(lineB) == 0:
        return []

    if len(lineA) == 0:
        return lineB[::]

    if len(lineB) == 0:
        return lineA[::]

    if lineA[-1] < lineB[-1]:
        lineA, lineB = lineB, lineA

    segACount = len(lineA) // 2
    segBCount = len(lineB) // 2

    union = []

    def addSeg(seg):
        union.append(seg[0])
        union.append(seg[1])

    segBInd = 0
    segB = get_seg(lineB, segBInd)

    point_from = Point(float("inf"), {}, Vec3(0, 1, 0))
    point_to = Point(float("inf"), {}, Vec3(0, 1, 0))

    i = 0
    while i < segACount:
        segA = get_seg(lineA, i)

        if point_to == segB[1] and point_to < segA[0]:
            addSeg([point_from, point_to])
            point_from = point_to = Point(float("inf"), {})
            segBInd += 1
            if segBInd >= segBCount:
                break
            segB = get_seg(lineB, segBInd)

        if point_to != segB[1]:
            while segB[1] < segA[0]:
                addSeg(segB)
                segBInd += 1
                if segBInd >= segBCount:
                    break
                segB = get_seg(lineB, segBInd)

            if segBInd >= segBCount:
                break

        point_from = min_point(segA[0], segB[0], point_from)

        j = segBInd
        while j < segBCount:
            if get_seg(lineB, j)[1] >= segA[1]:
                break
            j += 1

        segBInd = min(j, segBCount - 1)
        segB = get_seg(lineB, segBInd)

        if segB[1] <= segA[1]:
            point_to = segA[1]
            addSeg([point_from, point_to])
            i += 1
            break

        if segB[0] > segA[1]:
            point_to = segA[1]
            addSeg([point_from, point_to])
            point_from = point_to = Point(float("inf"), {})
            i += 1
            continue

        point_to = segB[1]
        i += 1

    while i < segACount:
        addSeg(get_seg(lineA, i))
        i += 1

    return union


def segments_intersection(lineA, lineB):
    if len(lineA) == 0 or len(lineB) == 0:
        return []

    if lineA[-1] < lineB[-1]:
        lineA, lineB = lineB, lineA

    segACount = len(lineA) // 2
    segBCount = len(lineB) // 2

    intersection = []

    def addSeg(seg):
        intersection.append(seg[0])
        intersection.append(seg[1])

    segBInd = 0
    segB = get_seg(lineB, segBInd)

    for i in range(0, segACount):
        segA = get_seg(lineA, i)

        while segB[1] < segA[0]:
            segBInd += 1
            if segBInd >= segBCount:
                break
            segB = get_seg(lineB, segBInd)

        if segBInd >= segBCount:
            break

        while segB[1] <= segA[1]:
            addSeg([max_point(segA[0], segB[0]), min_point(segA[1], segB[1])])
            segBInd += 1
            if segBInd >= segBCount:
                break
            segB = get_seg(lineB, segBInd)

        if segBInd >= segBCount:
            break

        if segB[0] <= segA[1]:
            addSeg([max_point(segA[0], segB[0]), min_point(segA[1], segB[1])])

    return intersection


def segments_difference(lineA, lineB):
    if len(lineB) == 0:
        return lineA[::]

    segACount = len(lineA) // 2
    segBCount = len(lineB) // 2

    difference = []

    def addSeg(seg):
        difference.append(seg[0])
        difference.append(seg[1])

    for i in lineB:
        i.reverse_normal()

    segBInd = 0
    segB = get_seg(lineB, segBInd)

    point_from = Point(float("inf"), {}, Vec3(0, 1, 0))
    point_to = Point(float("inf"), {}, Vec3(0, 1, 0))

    i = 0
    while i < segACount:
        segA = get_seg(lineA, i)

        while segB[1] < segA[0]:
            segBInd += 1
            if segBInd >= segBCount:
                break
            segB = get_seg(lineB, segBInd)

        if segBInd >= segBCount:
            break

        if segA[1] < segB[0]:
            addSeg(segA)
            i += 1
            continue

        if segA[0] < segB[0]:
            addSeg([segA[0], segB[0]])

        if segA[1] < segB[1]:
            i += 1
            continue

        point_from = segB[1]
        segBInd += 1
        if segBInd < segBCount:
            segB = get_seg(lineB, segBInd)
            while segB[1] <= segA[1]:
                point_to = segB[0]
                addSeg([point_from, point_to])
                point_from = segB[1]
                segBInd += 1
                if segBInd >= segBCount:
                    break
                segB = get_seg(lineB, segBInd)

        if segBInd >= segBCount:
            addSeg([point_from, segA[1]])
            i += 1
            break

        if point_from < segA[1]:
            addSeg([point_from, min_point(segB[0], segA[1])])

    while i < segACount:
        addSeg(get_seg(lineA, i))
        i += 1

    return difference
