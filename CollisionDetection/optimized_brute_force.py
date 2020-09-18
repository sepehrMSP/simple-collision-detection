def cross(a1, a2, b1, b2, c1, c2, aa1, aa2, bb1, bb2, cc1, cc2):
    dXa = a1 - cc1
    dYa = a2 - cc2
    dXb = b1 - cc1
    dYb = b2 - cc2
    dXc = c1 - cc1
    dYc = c2 - cc2
    dX21 = cc1 - bb1
    dY12 = bb2 - cc2
    l = aa1 - cc1
    D = dY12 * (l) + dX21 * (aa2 - cc2)
    sa = dY12 * dXa + dX21 * dYa
    sb = dY12 * dXb + dX21 * dYb
    sc = dY12 * dXc + dX21 * dYc
    ll = cc2 - aa2
    ta = (ll) * dXa + (l) * dYa
    tb = (ll) * dXb + (l) * dYb
    tc = (ll) * dXc + (l) * dYc

    if D < 0:
        return ((sa >= 0 and sb >= 0 and sc >= 0) or
                (ta >= 0 and tb >= 0 and tc >= 0) or
                (sa + ta <= D and sb + tb <= D and sc + tc <= D))

    return ((sa <= 0 and sb <= 0 and sc <= 0) or
            (ta <= 0 and tb <= 0 and tc <= 0) or
            (sa + ta >= D and sb + tb >= D and sc + tc >= D))


def intersection(a1, a2, b1, b2, c1, c2, aa1, aa2, bb1, bb2, cc1, cc2):
    return not (cross(a1, a2, b1, b2, c1, c2, aa1, aa2, bb1, bb2, cc1, cc2) or cross(aa1, aa2, bb1, bb2, cc1, cc2, a1,
                                                                                     a2, b1, b2, c1, c2))


for temp in range(30):
    t1 = []
    while True:
        inp = input().split()
        if inp[0] == 'end1':
            break
        coord = tuple(map(int, inp))
        t1.append(coord)

    flag = True
    while True:
        inp = input().split()
        if inp[0] == 'end2':
            break
        coord = tuple(map(int, inp))
        if flag:
            for t in t1:
                if intersection(t[0], t[1], t[2], t[3], t[4], t[5], coord[0], coord[1], coord[2], coord[3], coord[4],
                                coord[5]):
                    print(1)
                    flag = False
                    break
    if flag:
        print(0)
