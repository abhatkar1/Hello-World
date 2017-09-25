# (The Rational class) Modify the Rational class in Listing 8.4, Rational.py, to
# throw a RuntimeError exception if the denominator is 0.

class Rational:
    def __init__(self, num=0, den=1):
        if den != 0:
            divisor = gcd(num, den)
            self.__numerator = (1 if den > 0 else -1) * int(num / divisor)
            self.__denominator = int(abs(den / divisor))
        else:
            raise RuntimeError("Demominator cannot be zero!")

    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    def __sub__(self, other):
        n = self.__numerator * other[1] - self.__denominator * other[0]
        d = self.__denominator * other[1]
        return Rational(n, d)

    def __mul__(self, other):
        n = self.__numerator * other[0]
        d = self.__denominator * other[1]
        return Rational(n, d)

    def __truediv__(self, other):
        n = self.__numerator * other[1]
        d = self.__denominator * other[0]
        return Rational(n, d)

    def __float__(self):
        return self.__numerator / self.__denominator

    def __int__(self):
        return int(float(self))

    def __str__(self):
        return str(self.__numerator) if self.__denominator == 1 else str(self.__numerator) + "/" + str(self.__denominator)

    def __getitem__(self, item):
        if item == 0:
            return self.__numerator
        elif item == 1:
            return self.__denominator

    def __cmp__(self, other):
        differenceRational = self.__sub__(other)
        if differenceRational[0] > 0:
            return 1
        elif differenceRational[0] < 0:
            return -1
        else:
            return 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

def gcd(a, b):

    if a < b:
        a, b = b, a

    if a % b == 0:
        return b

    divisor = int(b / 2)

    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        else:
            divisor -= 1

def test():
    try:
        rational = Rational(1,0)
    except RuntimeError as ex:
        print(ex)


test()