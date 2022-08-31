# www.hackerrank.com/challenges/class -2-find-the-torsional-angle/problem

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        # pass
        return Points((self.x-no.x), (self.y-no.y), (self.z-no.z))

    def dot(self, no):
        # pass
        x1 = self.x
        y1 = self.y
        z1 = self.z
        x2 = no.x
        y2 = no.y
        z2 = no.z
        return x1*x2 + y1*y2 + z1*z2

    def cross(self, no):
        # pass
        x1 = self.x
        y1 = self.y
        z1 = self.z
        x2 = no.x
        y2 = no.y
        z2 = no.z
        return Points((y1*z2-z1*y2), -1*(x1*z2-z1*x2), (x1*y2-y1*x2))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]
                                            ), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
