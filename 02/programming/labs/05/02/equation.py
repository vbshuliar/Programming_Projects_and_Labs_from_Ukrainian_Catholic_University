"""Equation."""


class Polynomial:
    """Polynomial."""

    def __init__(self, coeffs):
        """Receives information."""
        self.coeffs = list(coeffs).copy()
        for _ in self.coeffs.copy():
            if _ == 0:
                self.coeffs.pop(0)
            else:
                break

    def __repr__(self):
        """Brief information."""
        return f"Polynomial(coeffs={self.coeffs})"

    def degree(self):
        """Returns degree."""
        return len(self.coeffs) - 1

    def coeff(self, num):
        """Returns coeff."""
        return self.coeffs[len(self.coeffs) - 1 - num]

    def evalAt(self, x):
        """Returns result of the evaluation."""
        equation = ""
        for _ in range(len(self.coeffs), 0, -1):
            digit = f"+{self.coeffs[-_]}" if self.coeffs[-_] >= 0 else self.coeffs[-_]
            power = _ - 1 if _ > 1 else _
            num = "x" if _ > 1 else "1"
            equation += f"{digit}*({num}**({power}))"
        return eval(equation)

    def __eq__(self, obj):
        """Equal."""
        if len(self.coeffs) == 1:
            self = self.coeffs[0]
        return str(self) == str(obj)

    def __hash__(self):
        """Hashes."""
        return hash(str(self))

    def scaled(self, num):
        """Scales equation."""
        return Polynomial([_ * num for _ in self.coeffs])

    def derivative(self):
        """Derivative."""
        new = []
        for _ in range(len(self.coeffs), 1, -1):
            digit = f"+{self.coeffs[-_]}" if self.coeffs[-_] >= 0 else self.coeffs[-_]
            power = _ - 1 if _ > 1 else _
            new.append(eval(str(digit * power)))
        return Polynomial(new)

    def addPolynomial(self, obj):
        """Adds polynomial."""
        if isinstance(obj, Polynomial):
            new = []
            lst1, lst2 = self.coeffs.copy(), obj.coeffs.copy()
            temp = sorted([lst1, lst2], key=lambda x: len(x), reverse=True)
            a, b = temp[0], temp[1]
            while len(b) > 0:
                new.append(a[-1] + b[-1])
                a.pop(-1)
                b.pop(-1)
            new.extend(a)

            return Polynomial(new[::-1])
        return None

    def multiplyPolynomial(self, obj):
        """Multiplies polynomial equations."""
        lst1, lst2 = self.coeffs.copy(), obj.coeffs.copy()
        new = [0 * _ for _ in range(len(lst1) + len(lst2) - 1)]
        offset = 0
        while offset < len(lst2):
            for ind, el in enumerate(lst1):
                new[ind + offset] += el * lst2[offset]
            offset += 1
        return Polynomial(new)


class Quadratic(Polynomial):
    """Quadratic."""

    def __init__(self, coeffs):
        """Receives information."""
        if not isinstance(coeffs, list) or len(coeffs) != 3:
            raise ValueError()
        for _ in coeffs:
            if not str(abs(_)).isdigit():
                raise ValueError()

        super().__init__(coeffs)

    def __repr__(self):
        """Brief information."""
        return f"Quadratic(a={self.coeffs[0]}, b={self.coeffs[1]}, c={self.coeffs[2]})"

    def discriminant(self):
        """Returns discriminant."""
        lst = self.coeffs
        a, b, c = lst[0], lst[1], lst[2]
        return b**2 - 4 * a * c

    def numberOfRealRoots(self):
        """Returns number or real roots."""
        if self.discriminant() > 0:
            return 2
        if self.discriminant() == 0:
            return 1
        return 0

    def getRealRoots(self):
        """Returns real roots."""
        lst = self.coeffs
        a, b, c, d = lst[0], lst[1], lst[2], self.discriminant()
        if self.numberOfRealRoots() == 0:
            return []
        if self.numberOfRealRoots() == 1:
            return [-b / (2 * a)]
        x1 = (-b - (d) ** (1 / 2)) / (2 * a)
        x2 = (-b + (d) ** (1 / 2)) / (2 * a)
        return sorted([round(x1), round(x2)])


def testPolynomialBasics():
    # we'll use a very simple str format...
    assert str(Polynomial([1, 2, 3])) == "Polynomial(coeffs=[1, 2, 3])"
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
    assert p1.degree() == 2

    # p.coeff(i) returns the coefficient for x**i
    assert p1.coeff(0) == 5
    assert p1.coeff(1) == -3
    assert p1.coeff(2) == 2

    # p.evalAt(x) returns the polynomial evaluated at that value of x
    assert p1.evalAt(0) == 5
    assert p1.evalAt(2) == 7


def testPolynomialEq():
    assert Polynomial([1, 2, 3]) == Polynomial([1, 2, 3])
    assert Polynomial([1, 2, 3]) != Polynomial([1, 2, 3, 0])
    assert Polynomial([1, 2, 3]) != Polynomial([1, 2, 0, 3])
    assert Polynomial([1, 2, 3]) != Polynomial([1, -2, 3])
    assert Polynomial([1, 2, 3]) != 42
    assert Polynomial([1, 2, 3]) != "Wahoo!"
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert Polynomial([42]) == 42


def testPolynomialConstructor():
    # If the list is empty, treat it the same as [0]
    assert Polynomial([]) == Polynomial([0])
    assert Polynomial([]) != Polynomial([1])
    # In fact, disregard all leading 0's in a polynomial
    assert Polynomial([0, 0, 0, 1, 2]) == Polynomial([1, 2])
    assert Polynomial([0, 0, 0, 1, 2]).degree() == 1

    # Require that the constructor be non-destructive
    coeffs = [0, 0, 0, 1, 2]
    assert Polynomial(coeffs) == Polynomial([1, 2])
    assert coeffs == [0, 0, 0, 1, 2]

    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert Polynomial(coeffs) == Polynomial([1, 2])


def testPolynomialInSets():
    s = set()
    assert Polynomial([1, 2, 3]) not in s
    s.add(Polynomial([1, 2, 3]))
    assert Polynomial([1, 2, 3]) in s
    assert Polynomial([1, 2, 3]) in s
    assert Polynomial([1, 2]) not in s


def testPolynomialMath():
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5

    # p.scaled(scale) returns a new polynomial with all the
    # coefficients multiplied by the given scale
    p2 = p1.scaled(10)  # 20x**2 - 30x + 50
    assert isinstance(p2, Polynomial)
    assert p2.evalAt(0) == 50
    assert p2.evalAt(2) == 70

    # p.derivative() will return a new polynomial that is the derivative
    # of the original, using the power rule:
    # More info: https://www.mathsisfun.com/calculus/power-rule.html
    p3 = p1.derivative()  # 4x - 3
    assert type(p3) == Polynomial
    assert str(p3) == "Polynomial(coeffs=[4, -3])"
    assert p3.evalAt(0) == -3
    assert p3.evalAt(2) == 5

    # we can add polynomials together, which will add the coefficients
    # of any terms with the same degree, and return a new polynomial
    p4 = p1.addPolynomial(p3)  # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
    assert type(p4) == Polynomial
    assert str(p4) == "Polynomial(coeffs=[2, 1, 2])"
    assert p1 == Polynomial([2, -3, 5])
    assert p4.evalAt(2) == 12
    assert p4.evalAt(5) == 57
    # can't add a string and a polynomial!
    assert p1.addPolynomial("woo") == None

    # lastly, we can multiple polynomials together, which will multiply the
    # coefficients of two polynomials and return a new polynomial with the
    # correct coefficients.
    # More info: https://www.mathsisfun.com/algebra/polynomials-multiplying.html

    p1 = Polynomial([1, 3])
    p2 = Polynomial([1, -3])
    p3 = Polynomial([1, 0, -9])
    assert p1.multiplyPolynomial(p2) == p3  # (x + 3)(x - 3) == (x**2 - 9)
    assert p1 == Polynomial([1, 3])

    # (x**2 + 2)(x**4 + 3x**2) == (x**6 + 5x**4 + 6x**2)
    p1 = Polynomial([1, 0, 2])
    p2 = Polynomial([1, 0, 3, 0, 0])
    p3 = Polynomial([1, 0, 5, 0, 6, 0, 0])
    assert p1.multiplyPolynomial(p2) == p3


def testPolynomialClass():
    print("Testing Polynomial class...", end="")
    testPolynomialBasics()
    testPolynomialEq()
    testPolynomialConstructor()
    testPolynomialInSets()
    testPolynomialMath()
    print("Passed!")


def testQuadraticClass():
    import math

    print("Testing Quadratic class...", end="")
    # Quadratic should inherit properly from Polynomial
    q1 = Quadratic([3, 2, 1])  # 3x^2 + 2x + 1
    assert type(q1) == Quadratic
    assert isinstance(q1, Quadratic) and isinstance(q1, Polynomial)
    assert q1.evalAt(10) == 321
    assert str(q1) == "Quadratic(a=3, b=2, c=1)"

    # We use the quadratic formula to find the function's roots.
    # More info: https://www.mathsisfun.com/quadratic-equation-solver.html

    # the discriminant is b**2 - 4ac
    assert q1.discriminant() == -8
    # use the discriminant to determine how many real roots (zeroes) exist
    assert q1.numberOfRealRoots() == 0
    assert q1.getRealRoots() == []

    # Once again, with a double root
    q2 = Quadratic([1, -6, 9])
    assert q2.discriminant() == 0
    assert q2.numberOfRealRoots() == 1
    [root] = q2.getRealRoots()
    assert math.isclose(root, 3)
    assert str(q2) == "Quadratic(a=1, b=-6, c=9)"

    # And again with two roots
    q3 = Quadratic([1, 1, -6])
    assert q3.discriminant() == 25
    assert q3.numberOfRealRoots() == 2
    [root1, root2] = q3.getRealRoots()  # smaller one first
    assert math.isclose(root1, -3) and math.isclose(root2, 2)

    # Creating a non-quadratic "Quadratic" is an error
    ok = False  # the exception turns this to True!
    try:
        q = Quadratic([1, 2, 3, 4])  # this is cubic, should fail!
    except:
        ok = True
    assert ok
    # one more time, with a line, which is sub-quadratic, so also fails
    ok = False
    try:
        q = Quadratic([2, 3])
    except:
        ok = True
    assert ok

    # And make sure that these methods were defined in the Quadratic class
    # and not in the Polynomial class (we'll just check a couple of them...)
    assert "evalAt" in Polynomial.__dict__
    assert "evalAt" not in Quadratic.__dict__
    assert "discriminant" in Quadratic.__dict__
    assert "discriminant" not in Polynomial.__dict__
    print("Passed!")


def testEquationClasses():
    testPolynomialClass()
    testQuadraticClass()


if __name__ == "__main__":
    testEquationClasses()
