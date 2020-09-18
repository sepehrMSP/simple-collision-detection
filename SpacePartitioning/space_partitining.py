# quad tree
def has_intersect(rect1, rect2):
    if not rect1[1] <= rect2[0]:
        if not rect2[1] <= rect1[0]:
            if not rect1[3] <= rect2[2]:
                if not rect2[3] <= rect1[2]:
                    return True
    else:
        return False


class QuadTree:

    def __init__(self, x_min, x_max, y_min, y_max):
        self.rectangles = []

        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.up_left = None
        self.up_right = None
        self.down_left = None
        self.down_right = None

    def set_child(self):
        if self.down_right or self.down_left or self.up_right or self.up_left:
            return
        else:
            x_min = self.x_min
            x_max = self.x_max
            y_min = self.y_min
            y_max = self.y_max
            y_mid = (y_min + y_max) / 2
            x_mid = (x_min + x_max) / 2
            self.up_left = QuadTree(x_min, x_mid, y_mid, y_max)
            self.up_right = QuadTree(x_mid, x_max, y_mid, y_max)
            self.down_left = QuadTree(x_min, x_mid, y_min, y_mid)
            self.down_right = QuadTree(x_mid, x_max, y_min, y_mid)

    def insert(self, rectangle):
        x_min = self.x_min
        x_max = self.x_max
        y_min = self.y_min
        y_max = self.y_max
        y_mid = (y_min + y_max) / 2
        x_mid = (x_max + x_min) / 2

        if rectangle[0] >= x_min and rectangle[1] <= x_mid and rectangle[2] >= y_mid and rectangle[3] <= y_max:
            self.set_child()
            self.up_left.insert(rectangle)
        elif rectangle[0] >= x_mid and rectangle[1] <= x_max and rectangle[2] >= y_mid and rectangle[3] <= y_max:
            self.set_child()
            self.up_right.insert(rectangle)
        elif rectangle[0] >= x_min and rectangle[1] <= x_mid and rectangle[2] >= y_min and rectangle[3] <= y_mid:
            self.set_child()
            self.down_left.insert(rectangle)
        elif rectangle[0] >= x_mid and rectangle[1] <= x_max and rectangle[2] >= y_min and rectangle[3] <= y_mid:
            self.set_child()
            self.down_right.insert(rectangle)
        else:
            self.rectangles.append(rectangle)

    def find_all_intersections(self, parent_recs=[]):
        # with it self
        big_recs = self.rectangles
        for i in range(len(big_recs)):
            for j in range(i + 1, len(big_recs)):
                if has_intersect(big_recs[i], big_recs[j]):
                    print(big_recs[i][4], big_recs[j][4])
        # with its parents rectangles
        for rect1 in big_recs:
            for rect2 in parent_recs:
                if has_intersect(rect1, rect2):
                    print(rect1[4], rect2[4])
        parent_recs += big_recs
        try:
            self.up_left.find_all_intersections(parent_recs)
        except:
            pass
        try:
            self.up_right.find_all_intersections(parent_recs)
        except:
            pass
        try:
            self.down_right.find_all_intersections(parent_recs)
        except:
            pass
        try:
            self.down_left.find_all_intersections(parent_recs)
        except:
            pass


index = 0
root = QuadTree(0, 1000, 0, 1000)
while True:
    try:
        rect = list(map(float, input().split()))
        rect[0] += 1000
        rect[1] += 1000
        rect[2] += 1000
        rect[3] += 1000
        rect.append(index)
        index += 1
        root.insert(rect)
    except:
        break

root.find_all_intersections()