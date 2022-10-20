"""
In computer science and computer programming, a data type (or simply type) is a "set" of possible values and a "set" of
allowed operations on it.
https://en.wikipedia.org/wiki/Data_type

A set is the mathematical model for a collection of different things; a set contains elements or members, which can be
mathematical objects of any kind: numbers, symbols, points in space, lines, other geometrical shapes, variables, or
even other sets. The set with no element is the empty set; a set with a single element is a singleton. A set may have
a finite number of elements or be an infinite set. Two sets are equal if they have precisely the same elements.

Sets are ubiquitous in modern mathematics. Indeed, set theory, more specifically Zermelo–Fraenkel set theory, has been
the standard way to provide rigorous foundations for all branches of mathematics since the first half of the 20th
century.
https://en.wikipedia.org/wiki/Set_(mathematics)
"""
from copy import deepcopy
import math

from operations import add_num, sub_num, mul_num, div_num
from operations import add_int, sub_int, mul_int

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

    # Type operations defined as static methods
    add = add_num
    sub = sub_num
    mul = mul_num
    div = div_num

    def __init__(self, data=0):
        if isinstance(data, int):
            self.data = data
        elif isinstance(data, Num):
            self.data = deepcopy(data.data)
        else:
            raise TypeError(f"Cannot create Num from {data}")
        assert self.data >= 0, f"Num is not defined for values less than 0. Got {data}"

    # Is this an operation?
    def successor(self):
        return self + 1

    def _verify(self, other):
        if isinstance(other, Num):
            return other
        elif isinstance(other, int):
            return Num(other)
        else:
            raise TypeError(f"Cannot operate on {self} and {other}")

    def __add__(self, other):
        other = self._verify(other)
        return Num.add(self, other)

    def __sub__(self, other):
        other = self._verify(other)
        assert self >= other, f"{self} - {other} is only defined if n > m"
        return Num.sub(self, other)

    def __mul__(self, other):
        other = self._verify(other)
        return Num.mul(self, other)

    # TODO: This needs to be reviewed, don't like current implementation
    def __truediv__(self, other):
        other = self._verify(other)
        left = self.data / other.data
        right = self.data // other.data
        assert left == right, "m / n is only defined if n is a factor of m"
        return Num.div(self.data, other.data)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    # TODO: refactor this
    def __eq__(self, other):
        """== operator
        n = m <=> The 1's in n can be paired up with the 1's in m.
        """
        other = self._verify(other)
        return self.data == other.data

    # TODO: refactor this
    def __lt__(self, other):
        """< operator
        n < m <=> n comes before m in the sequence of natural numbers.
        """
        other = self._verify(other)
        return self.data < other.data

    # TODO: refactor this
    def __gt__(self, other):
        """> operator
        n > m <=> n comes after m in the sequence of natural numbers.
        """
        other = self._verify(other)
        return self.data > other.data

    # TODO: refactor this
    def __le__(self, other):
        """<= operator
        n <= m <=> n comes before or is equal to m in the sequence of natural numbers.
        """
        other = self._verify(other)
        return self.data <= other.data

    # TODO: refactor this
    def __ge__(self, other):
        """>= operator
        n >= m <=> n comes after or is equal to m in the sequence of natural numbers.
        """
        other = self._verify(other)
        return self.data >= other.data

    def __str__(self):
        return f"N({self.data})"


class Int:
    """
    Definition: An integer is an ordered pair (m, n) of natural numbers, written m\n.
    """

    # Type operations defined as static methods
    add = add_int
    sub = sub_int
    mul = mul_int

    def __init__(self, data=(0, 0)):
        if isinstance(data, tuple):
            assert len(data) == 2, f"input = {data} needs to be a tuple of length 2"
            self.data = (Num(data[0]), Num(data[1]))
        elif isinstance(data, Int):
            self.data = deepcopy(data.data)
        else:
            raise ValueError(
                f"input = {data} needs to be a tuple of ints or Num or just an Int"
            )

    def _verify(self, other):
        if isinstance(other, Int):
            return other
        elif isinstance(other, tuple):
            return Int(other)
        else:
            raise TypeError(f"Cannot operate on {self} and {other}")

    def __add__(self, other):
        self._verify(other)
        return Int.add(self, other)

    def __sub__(self, other):
        self._verify(other)
        return Int.sub(self, other)

    def __mul__(self, other):
        self._verify(other)
        return Int.mul(self, other)

    def __eq__(self, other):
        """== operator
        Definition: Integers m | n and k | l are equal <=> m + l = n + k.
        """
        self._verify(other)
        m, n, k, l = self.m, self.n, other.m, other.n
        return (m + l) == (n + k)

    def __str__(self):
        return f"I({self.m.data-self.n.data})"


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
    # assert laws_of_multiplication(a, b, c)
    # assert laws_of_subtraction(a, b, c)
    # assert laws_of_division(a, b, c)
    # assert distributive_law(a, b, c)
    print("Natural Numbers passed")

    # Integers
    # a = Int(-1)
    # b = Int(-5)
    # c = Int(3)
    # assert Int(-5) == Int(-1) + Int(-4)
    # assert Int(-5) == Int(1, 6)
    # assert laws_of_addition(a, b, c)
    # assert laws_of_multiplication(a, b, c)
    # assert laws_of_subtraction(a, b, c)
    # assert distributive_law(a, b, c)
    # print("Integers passed")

    """
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
    """

    print("All tests passed")
