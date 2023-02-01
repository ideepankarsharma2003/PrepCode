# www.hackerrank.com/challenges/class -1-dealing-with -complex-numbers/problem

import math


class Complex(object):
    def __init__(self, real, imaginary):
        # print(f'real= {real}  {type(real)}')
        # print(f'imaginaryl= {imaginary}  {type(imaginary)}')
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        # pass
        r = self.real+no.real
        i = self.imaginary+no.imaginary
        if i >= 0:
            return "{:.2f}".format(r) + '+' + "{:.2f}".format(i) + 'i'
        return "{:.2f}".format(r) + "{:.2f}".format(i) + 'i'

    def __sub__(self, no):
        # pass
        r = self.real-no.real
        i = self.imaginary-no.imaginary
        if i >= 0:
            return "{:.2f}".format(r) + '+' + "{:.2f}".format(i) + 'i'
        return "{:.2f}".format(r) + "{:.2f}".format(i) + 'i'

    def __mul__(self, no):
        # pass
        r = (self.real*no.real)-(self.imaginary*no.imaginary)
        i = (self.real*no.imaginary)+(self.imaginary*no.real)
        if i >= 0:
            return "{:.2f}".format(r) + '+' + "{:.2f}".format(i) + 'i'
        return "{:.2f}".format(r) + "{:.2f}".format(i) + 'i'

    def __truediv__(self, no):
        # pass
        cdsq = no.imaginary**2 + no.real**2
        r = ((self.real*no.real)+(self.imaginary*no.imaginary))/cdsq
        i = ((self.imaginary*no.real)-(self.real*no.imaginary))/cdsq
        if i >= 0:
            return "{:.2f}".format(r) + '+' + "{:.2f}".format(i) + 'i'
        return "{:.2f}".format(r) + "{:.2f}".format(i) + 'i'

    def mod(self):
        # pass
        r = (self.real**2 + self.imaginary**2)**0.5
        i = 0
        if i >= 0:
            return "{:.2f}".format(r) + '+' + "{:.2f}".format(i) + 'i'
        return "{:.2f}".format(r) + "{:.2f}".format(i) + 'i'

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
