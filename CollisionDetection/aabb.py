import sys

class Triangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def getx(self, i):
        if i == 0:
            return self.x1
        if i == 1:
            return self.x2
        else:
            return self.x3

    def gety(self, i):
        if i == 0:
            return self.y1
        if i == 1:
            return self.y2
        else:
            return self.y3

    def get(self, i):
        return self.getx(i), self.gety(i)

    def __str__(self):
        return self.x1.__str__() + " " + self.y1.__str__() + " " + self.x2.__str__() + " " + self.y2.__str__() + " " + self.x3.__str__() + " " + self.y3.__str__()


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class AABB:
    def __init__(self, max_x: int, max_y: int, min_x: int, min_y: int, triangle: Triangle = None):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y
        self.triangle = triangle

    def get_area(self):
        return (self.max_x - self.min_x) * (self.max_y - self.min_y)

    def get_perimeter(self):
        return 2 * ((self.max_x - self.min_x) + (self.max_y - self.min_y))

    # can be optimized
    def contain(self, other):
        if self.min_y < other.min_y and self.max_y > other.max_y and self.min_x < other.min_x and self.max_x > other.max_x:
            return True
        else:
            return False

    def intersection(self, other):
        return not (
                self.max_x < other.min_x or self.min_x > other.max_x or self.max_y < other.min_y or self.min_y > other.max_y)


class Node:
    def __init__(self, aabb: AABB = None):
        self.parent = None
        self.aabb = aabb
        self.left = None
        self.right = None

    def is_leaf(self):
        if not self.right and not self.left:
            return True
        else:
            return False


def heuristic(node1: Node, node2: Node):
    if not node1:
        return node2.aabb.get_area()
    if not node2:
        return node1.aabb.get_area()

    max_x = max(node1.aabb.max_x, node2.aabb.max_x)
    max_y = max(node1.aabb.max_y, node2.aabb.max_y)
    min_y = min(node1.aabb.min_y, node2.aabb.min_y)
    min_x = min(node1.aabb.min_x, node2.aabb.min_x)
    return (max_x - min_x) * (max_y - min_y)


def insert(root: Node, node: Node):
    if root is None:
        return node

    elif not root.right and not root.left:
        new_parent = Node()
        new_parent.parent = root.parent
        new_parent.left = root
        new_parent.right = node
        max_x = max(node.aabb.max_x, root.aabb.max_x)
        max_y = max(node.aabb.max_y, root.aabb.max_y)
        min_x = min(node.aabb.min_x, root.aabb.min_x)
        min_y = min(node.aabb.min_y, root.aabb.min_y)
        new_parent.aabb = AABB(max_x, max_y, min_x, min_y)
        if root.parent:
            if new_parent.parent.left == root:
                new_parent.parent.left = new_parent
            else:
                new_parent.parent.right = new_parent

        new_parent.right.parent = new_parent
        new_parent.left.parent = new_parent

        return new_parent

    else:
        cost1 = heuristic(root.left, node)
        cost2 = heuristic(root.right, node)
        if cost1 <= cost2:
            insert(root.left, node)
        else:
            insert(root.right, node)

    # now balance the aabb tree
    right = root.right
    left = root.left
    if root.aabb.contain(right.aabb) and root.aabb.contain(left.aabb):
        return root
    else:
        new_root = Node()
        new_root.right = right
        new_root.left = left
        min_x = min(right.aabb.min_x, left.aabb.min_x)
        min_y = min(right.aabb.min_y, left.aabb.min_y)
        max_x = max(right.aabb.max_x, left.aabb.max_x)
        max_y = max(right.aabb.max_y, left.aabb.max_y)
        new_root.aabb = AABB(max_x, max_y, min_x, min_y)
        right.parent = new_root
        left.parent = new_root
        return new_root


def aabb_intersection(aabb1: AABB, aabb2: AABB):
    if aabb2.max_x >= aabb1.min_x >= aabb2.min_x and aabb2.max_y >= aabb1.min_y >= aabb2.min_y:
        return True
    if aabb2.max_x >= aabb1.min_x >= aabb2.min_x and aabb2.max_y >= aabb1.max_y >= aabb2.min_y:
        return True
    if aabb2.max_x >= aabb1.max_x >= aabb2.min_x and aabb2.max_y >= aabb1.min_y >= aabb2.min_y:
        return True
    if aabb2.max_x >= aabb1.max_x >= aabb2.min_x and aabb2.max_y >= aabb1.max_y >= aabb2.min_y:
        return True

    if aabb1.max_x >= aabb2.min_x >= aabb1.min_x and aabb1.max_y >= aabb2.min_y >= aabb1.min_y:
        return True
    if aabb1.max_x >= aabb2.min_x >= aabb1.min_x and aabb1.max_y >= aabb2.max_y >= aabb1.min_y:
        return True
    if aabb1.max_x >= aabb2.max_x >= aabb1.min_x and aabb1.max_y >= aabb2.min_y >= aabb1.min_y:
        return True
    if aabb1.max_x >= aabb2.max_x >= aabb1.min_x and aabb1.max_y >= aabb2.max_y >= aabb1.min_y:
        return True
    return False


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


def triangle_intersection(triangle1: Triangle, triangle2: Triangle):
    # if not (cross(triangle1, triangle2) or cross(triangle2, triangle1)):
    #     print(triangle1.__str__() + "\n" + triangle2.__str__())
    return not (cross(triangle1, triangle2) or cross(triangle2, triangle1))


# def cross(a, b):
#     return a[0] * b[1] - a[1] * b[0]
#
#
# def sub(a, b):
#     return a[0] - b[0], a[1] - b[1]
#
#
# def check(A, B, x, y, z):
#     flag = cross(sub(A.get(x), A.get(y)), sub(A.get(z), A.get(y)))
#     for i in range(3):
#         c = cross(sub(A.get(x), A.get(y)), sub(B.get(i), A.get(y)))
#         if c == 0:
#             continue
#         if (flag > 0 and c > 0) or (flag < 0 and c < 0):
#             return False
#     return True
#
#
# def triangle_intersection(A, B):
#     if check(A, B, 1, 0, 2) or check(A, B, 2, 1, 0) or check(A, B, 0, 2, 1) \
#             or check(B, A, 1, 0, 2) or check(B, A, 2, 1, 0) or check(B, A, 0, 2, 1):
#         return False
#     return True


def intersection(node1: Node, node2: Node):
    if node1.is_leaf() and node2.is_leaf():
        return triangle_intersection(node1.aabb.triangle, node2.aabb.triangle)

    if not aabb_intersection(node1.aabb, node2.aabb):
        return False
    else:
        if node1.left and node1.right:
            if node2.left and node2.right:
                if aabb_intersection(node1.left.aabb, node2.left.aabb):
                    if intersection(node1.left, node2.left):
                        return True
                if aabb_intersection(node1.left.aabb, node2.right.aabb):
                    if intersection(node1.left, node2.right):
                        return True
                if aabb_intersection(node1.right.aabb, node2.left.aabb):
                    if intersection(node1.right, node2.left):
                        return True
                if aabb_intersection(node1.right.aabb, node2.right.aabb):
                    if intersection(node1.right, node2.right):
                        return True
                return False
        if node1.right and node1.left:
            if node2.is_leaf():
                if aabb_intersection(node1.right.aabb, node2.aabb):
                    if intersection(node1.right, node2):
                        return True
                if aabb_intersection(node1.left.aabb, node2.aabb):
                    if intersection(node1.left, node2):
                        return True
                return False
        if node2.right and node2.left:
            if node1.is_leaf():
                if aabb_intersection(node2.right.aabb, node1.aabb):
                    if intersection(node2.right, node1):
                        return True
                if aabb_intersection(node2.left.aabb, node1.aabb):
                    if intersection(node2.left, node1):
                        return True
                    return False


for temp in range(30):
    root1 = None
    root2 = None
    triangle1 = None
    triangle2 = None

    while True:
        inp = input().strip().split(' ')
        if inp[0] == 'end1':
            break
        coord = list(map(int, inp))
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]
        x3 = coord[4]
        y3 = coord[5]

        triangle1 = Triangle(x1, y1, x2, y2, x3, y3)
        max_x = max(x1, x2, x3)
        min_x = min(x1, x2, x3)
        max_y = max(y1, y2, y3)
        min_y = min(y1, y2, y3)
        aabb = AABB(max_x, max_y, min_x, min_y, triangle1)
        node = Node(aabb)
        root1 = insert(root1, node)

    while True:
        inp = input().strip().split(' ')
        if inp[0] == 'end2':
            break
        coord = list(map(int, inp))
        x1 = coord[0]
        y1 = coord[1]
        x2 = coord[2]
        y2 = coord[3]
        x3 = coord[4]
        y3 = coord[5]

        triangle2 = Triangle(x1, y1, x2, y2, x3, y3)
        max_x = max(x1, x2, x3)
        min_x = min(x1, x2, x3)
        max_y = max(y1, y2, y3)
        min_y = min(y1, y2, y3)
        aabb = AABB(max_x, max_y, min_x, min_y, triangle2)
        node = Node(aabb)
        root2 = insert(root2, node)

    if intersection(root1, root2):
        print(1)
    else:
        print(0)
# if triangle_intersection(triangle1, triangle2):
#     print(1)
# else:
#     print(0)
