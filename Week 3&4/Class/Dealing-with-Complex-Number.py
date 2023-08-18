#Problem LInk: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?isFullScreen=true
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        rl = self.real + no.real
        img = self.imaginary + no.imaginary
        return Complex(rl,img)
        
    def __sub__(self, no):
        rl = self.real - no.real
        img = self.imaginary - no.imaginary
        return Complex(rl,img)
        
    def __mul__(self, no):
        rl = (self.real*no.real) - (self.imaginary * no.imaginary)
        img = (self.real*no.imaginary) + (self.imaginary * no.real)
        return Complex(rl,img)

    def __truediv__(self, no):
        rl = (self.real*no.real) + (self.imaginary * no.imaginary)
        img = (self.imaginary * no.real) - (self.real*no.imaginary)
        rl /= (no.real * no. real) + (no.imaginary * no.imaginary)
        img /= (no.real * no. real) + (no.imaginary * no.imaginary) 
        return Complex(rl,img)

    def mod(self):
        return Complex(math.sqrt((self.real**2) + (self.imaginary**2)),0)

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