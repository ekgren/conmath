import math

from theorems import (
    laws_of_addition,
    laws_of_multiplication,
    laws_of_subtraction,
    laws_of_division,
    distributive_law,
)


############################################################
# Type implementations
############################################################


class Num:
    """Natural Number
    Definition: A natural number is a string of 1's.
    1, 11, 111, 1111, 11111, ...
    In this implementation we choose to represent a natural number with
    the Hindu-Arabic number system as an integer.
    """

    def __init__(self, input):
        data = input.data if isinstance(input, Num) else input
        assert isinstance(data, int), f"data = {data} needs to be int"
        assert data >= 0, f"data = {data} needs to be >= 0"
        self.data = data

    def successor(self):
        return Num(self + 1)

    def __add__(self, other):
        """Addition or the + operator.
        Definition: The sum of n and m is the combination of the 1's in n and m.
        It is written n + m."""
        other = other if isinstance(other, Num) else Num(other)
        return Num(self.data + other.data)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        """Subtraction (the inverse of addition) or the - operator.
        n - m <=> The number of 1's in n that are not in m.
        """
        other = other if isinstance(other, Num) else Num(other)
        assert (
            self.data >= other.data
        ), f"{self.data} - {other.data} is only defined if n > m"
        return Num(self.data - other.data)

    def __mul__(self, other):
        """* operator
        Definition: The product of numbers n and m is the string formed by a copy
        of m for every 1 in n. It is written n * m.
        """
        other = other if isinstance(other, Num) else Num(other)
        return Num(self.data * other.data)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        """/ operator
        n / m <=> The number of times m can be subtracted from n.
        """
        other = other if isinstance(other, Num) else Num(other)
        assert (
            self.data / other.data == self.data // other.data
        ), f"{self.data} / {other.data} is only defined if m is a factor of n"
        assert other.data != 0, "Division by zero is undefined"
        return Num(self.data // other.data)

    def __eq__(self, other):
        """== operator
        n = m <=> The 1's in n can be paired up with the 1's in m.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data == other.data

    def __lt__(self, other):
        """< operator
        n < m <=> n comes before m in the sequence of natural numbers.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data < other.data

    def __gt__(self, other):
        """> operator
        n > m <=> n comes after m in the sequence of natural numbers.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data > other.data

    def __le__(self, other):
        """<= operator
        n <= m <=> n comes before or is equal to m in the sequence of natural numbers.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data <= other.data

    def __ge__(self, other):
        """>= operator
        n >= m <=> n comes after or is equal to m in the sequence of natural numbers.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data >= other.data

    def __str__(self):
        return f"N({self.data})"


class Fra:
    """
    Definition: A fraction is an ordered pair (m, n) of natural numbers, also written m / n.
    """

    def __init__(self, m, n, normalize=True):
        m = m if isinstance(m, Num) else Num(m)
        n = n if isinstance(n, Num) else Num(n)
        self.m = m
        self.n = n
        if normalize:
            self.normalize()

    def __add__(self, other):
        """Addition or the + operator.
        Definition: The sum of fractions a / b and c / d is the fraction (ad + bc) / bd.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        m = self.m * other.n + self.n * other.m
        n = self.n * other.n
        return Fra(m, n)

    def __sub__(self, other):
        """Subtraction or the - operator.
        Definition: The difference of fractions a / b and c / d is the fraction (ad - bc) / bd.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return Fra(self.m * other.n - self.n * other.m, self.n * other.n)

    def __mul__(self, other):
        """Multiplication or the * operator.
        Definition: The product of fractions a / b and c / d is the fraction ac / bd.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return Fra(self.m * other.m, self.n * other.n)

    def __truediv__(self, other):
        """Division or the / operator.
        Definition: The quotient of fractions a / b and c / d is the fraction ad / bc.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return Fra(self.m * other.n, self.n * other.m)

    def __eq__(self, other):
        """== operator
        (m, n) = (p, q) <=> m * q = n * p
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return (self.m * other.n) == (self.n * other.m)

    def __str__(self):
        return f"F({self.m.data}/{self.n.data})"

    def normalize(self):
        """Normalizes the fraction"""
        gcd = math.gcd(self.m.data, self.n.data)
        while gcd > 1:
            self.m.data //= gcd
            self.n.data //= gcd
            gcd = math.gcd(self.m.data, self.n.data)


class Int:
    """
    Definition: An integer is an ordered pair (m, n) of natural numbers, written m\n.
    """

    def __init__(self, m, n=None):
        # Accepts two input forms. If n is not provided, then m can be a negative int.
        # If n is provided, then m must be a positive int or Num.
        if n is None:
            if isinstance(m, int):
                if m <= 0:
                    n = abs(m) + 1
                    m = 1
                else:
                    m = m + 1
                    n = 1
            elif isinstance(m, Num):
                m = m + 1
                n = 1
            else:
                raise ValueError(f"m = {m} needs to be int or Num")
        else:
            m = m
            n = n

        self.m = m if isinstance(m, Num) else Num(m)
        self.n = n if isinstance(n, Num) else Num(n)
        assert isinstance(self.m, Num), f"m = {self.m} needs to be Num"
        assert isinstance(self.n, Num), f"n = {self.n} needs to be Num"

    def __add__(self, other):
        """Addition or the + operator.
        Definition: The sum of integers m | n and k | l is the integer (m + k) | (n + l).
        """
        other = other if isinstance(other, Int) else Int(other)
        m, n, k, l = self.m, self.n, other.m, other.n
        return Int(m + k, n + l)

    def __sub__(self, other):
        """Subtraction or the - operator.
        Definition: The difference of integers m | n and k | l is the integer (m + l) | (n + k).
        """
        other = other if isinstance(other, Int) else Int(other)
        m, n, k, l = self.m, self.n, other.m, other.n
        return Int(m + l, n + k)

    def __mul__(self, other):
        """Multiplication or the * operator.
        Definition: The product of integers m | n and k | l is the integer (mk + nl) | (ml + nk).
        """
        other = other if isinstance(other, Int) else Int(other)
        m, n, k, l = self.m, self.n, other.m, other.n
        return Int(m * k + n * l, m * l + n * k)

    def __eq__(self, other):
        """== operator
        Definition: Integers m | n and k | l are equal <=> m + l = n + k.
        """
        other = other if isinstance(other, Int) else Int(other)
        m, n, k, l = self.m, self.n, other.m, other.n
        return (m + l) == (n + k)

    def __str__(self):
        return f"I({self.m.data-self.n.data})"

    def val(self):
        return self.m.data - self.n.data


class Rat:
    """
    Definition: A rational number is an ordered pair (a, b) a, b in Int, b != 0
    Written a/b [0 == 1 | 1]
    """

    def __init__(self, a, b=1):
        a = a if isinstance(a, Int) else Int(a)
        b = b if isinstance(b, Int) else Int(b)
        self.a = a
        self.b = b

    def __add__(self, other):
        """Addition or the + operator.
        Definition: The sum of rational numbers a / b and c / d is the rational number (a * d + b * c) / (b * d).
        """
        other = other if isinstance(other, Rat) else Rat(other)
        a, b, c, d = self.a, self.b, other.a, other.b
        return Rat(a * d + b * c, b * d)

    def __sub__(self, other):
        """Subtraction or the - operator.
        Definition: The difference of rational numbers a / b and c / d is the rational number (a * d - b * c) / (b * d).
        """
        other = other if isinstance(other, Rat) else Rat(other)
        a, b, c, d = self.a, self.b, other.a, other.b
        return Rat(a * d - b * c, b * d)

    def __mul__(self, other):
        """Multiplication or the * operator.
        Definition: The product of rational numbers a / b and c / d is the rational number (a * c) / (b * d).
        """
        other = other if isinstance(other, Rat) else Rat(other)
        a, b, c, d = self.a, self.b, other.a, other.b
        return Rat(a * c, b * d)

    def __truediv__(self, other):
        """Division or the / operator.
        Definition: The quotient of rational numbers a / b and c / d is the rational number (a * d) / (b * c).
        """
        other = other if isinstance(other, Rat) else Rat(other)
        a, b, c, d = self.a, self.b, other.a, other.b
        return Rat(a * d, b * c)

    def __eq__(self, other):
        """== operator
        a/b = c/d <=> a * d = b * c
        """
        other = other if isinstance(other, Rat) else Rat(other)
        a, b, c, d = self.a, self.b, other.a, other.b
        return (a * d) == (b * c)

    def __str__(self):
        if self.b.val == 1:
            return f"R({self.a.val})"
        elif self.a.val == 0:
            return f"R(0)"
        return f"R({self.a.val}/{self.b.val})"


if __name__ == "__main__":
    # Natural Numbers
    a = 1 + Num(4)
    b = Num(2)
    c = Num(2)
    assert laws_of_addition(a, b, c)
    assert laws_of_multiplication(a, b, c)
    assert laws_of_subtraction(a, b, c)
    assert laws_of_division(a, b, c)
    assert distributive_law(a, b, c)
    print("Natural Numbers passed")

    # Fractions
    a = Fra(4, 2)
    b = Fra(2, 2)
    c = Fra(2, 2)
    assert laws_of_addition(a, b, c)
    assert laws_of_multiplication(a, b, c)
    assert laws_of_subtraction(a, b, c)
    assert laws_of_division(a, b, c)
    assert distributive_law(a, b, c)
    print("Fractions passed")

    # Integers
    a = Int(-1)
    b = Int(-5)
    c = Int(3)
    assert Int(-5) == Int(-1) + Int(-4)
    assert Int(-5) == Int(1, 6)
    assert laws_of_addition(a, b, c)
    assert laws_of_multiplication(a, b, c)
    assert laws_of_subtraction(a, b, c)
    assert distributive_law(a, b, c)
    print("Integers passed")

    # Rational Numbers
    a = Rat(1, 3)
    b = Rat(1, 4)
    c = Rat(1, 5)
    assert laws_of_addition(a, b, c)
    assert laws_of_multiplication(a, b, c)
    assert laws_of_subtraction(a, b, c)
    assert laws_of_division(a, b, c)
    assert distributive_law(a, b, c)
    # assert field(a, b, c)
    print("Rational Numbers passed")

    print("All tests passed")
