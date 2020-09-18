class Triangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def cross(triangle1: Triangle, triangle2: Triangle):
    pa = Point(triangle1.x1, triangle1.y1)
    pb = Point(triangle1.x2, triangle1.y2)
    pc = Point(triangle1.x3, triangle1.y3)

    p0 = Point(triangle2.x1, triangle2.y1)
    p1 = Point(triangle2.x2, triangle2.y2)
    p2 = Point(triangle2.x3, triangle2.y3)

    dXa = pa.x - p2.x
    dYa = pa.y - p2.y
    dXb = pb.x - p2.x
    dYb = pb.y - p2.y
    dXc = pc.x - p2.x
    dYc = pc.y - p2.y
    dX21 = p2.x - p1.x
    dY12 = p1.y - p2.y
    D = dY12 * (p0.x - p2.x) + dX21 * (p0.y - p2.y)
    sa = dY12 * dXa + dX21 * dYa
    sb = dY12 * dXb + dX21 * dYb
    sc = dY12 * dXc + dX21 * dYc

    ta = (p2.y - p0.y) * dXa + (p0.x - p2.x) * dYa
    tb = (p2.y - p0.y) * dXb + (p0.x - p2.x) * dYb
    tc = (p2.y - p0.y) * dXc + (p0.x - p2.x) * dYc

    if D < 0:
        return ((sa >= 0 and sb >= 0 and sc >= 0) or
                (ta >= 0 and tb >= 0 and tc >= 0) or
                (sa + ta <= D and sb + tb <= D and sc + tc <= D))

    return ((sa <= 0 and sb <= 0 and sc <= 0) or
            (ta <= 0 and tb <= 0 and tc <= 0) or
            (sa + ta >= D and sb + tb >= D and sc + tc >= D))


def intersection(triangle1: Triangle, triangle2: Triangle):
    return not (cross(triangle1, triangle2) or cross(triangle2, triangle1))


coord = list(map(int, input().strip().split(' ')))
x1 = coord[0]
y1 = coord[1]
x2 = coord[2]
y2 = coord[3]
x3 = coord[4]
y3 = coord[5]
triangle1 = Triangle(x1, y1, x2, y2, x3, y3)

coord = list(map(int, input().strip().split(' ')))
x1 = coord[0]
y1 = coord[1]
x2 = coord[2]
y2 = coord[3]
x3 = coord[4]
y3 = coord[5]
triangle2 = Triangle(x1, y1, x2, y2, x3, y3)

if intersection(triangle1, triangle2):
    print(1)
else:
    print(0)
