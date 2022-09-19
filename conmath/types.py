############################################################
# We start with some laws of arithmetic
############################################################
def laws_of_addition(a, b, c):
    """ The laws of addition are: """

    def commutative(a, b):
        """ a + b = b + a       (Commutative) """
        return a + b == b + a

    def associative(a, b, c):
        """ (a + b) + c = a + (b + c)     (Associative) """
        return (a + b) + c == a + (b + c)

    return commutative(a, b) and associative(a, b, c)


def laws_of_multiplication(a, b, c):
    """ The laws of multiplication are: """

    def commutative(a, b):
        """ a * b = b * a       (Commutative) """
        return a * b == b * a

    def associative(a, b, c):
        """ (a * b) * c = a * (b * c)     (Associative) """
        return (a * b) * c == a * (b * c)

    def identity(a):
        """ a * 1 = a    (identity) """
        return a * 1 == a

    return commutative(a, b) and associative(a, b, c) and identity(a)


def laws_of_subtraction(a, b, c):
    """ The laws of subtraction are: """

    def law_one(a, b, c):
        return a - (b + c) == (a - b) - c

    def law_two(a, b):
        return a + (b - c) == (a + b) - c

    def law_three(a, b):
        return a - (b - c) == (a - b) + c

    return law_one(a, b, c) and law_two(a, b) and law_three(a, b)


def laws_of_division(a, b, c):
    """ The laws of division are: """

    def law_one(a, b):
        return a / b + c / b == (a + c) / b

    def law_two(a, b):
        return (b * a) / (b * c) == a / c

    return law_one(a, b) and law_two(a, b)


def distributive_law(a, b, c):
    """ a * (b + c) = (a * b) + (a * c)     (Distributive) """
    return a * (b + c) == (a * b) + (a * c) and (a + b) * c == (a * c) + (b * c)


############################################################
# Type implementations
############################################################


class Num:
    """ Natural Number
    Definition: A natural number is a string of 1's.
    1, 11, 111, 1111, 11111, ...
    In this implementation we choose to represent a natural number with
    the Hindu-Arabic number system as an integer.
    """
    def __init__(self, data):
        assert isinstance(data, int), f"data = {data} needs to be int"
        assert data >= 0, f"data = {data} needs to be >= 0"
        self.data = data

    def successor(self):
        return Num(self.data + 1)

    def __add__(self, other):
        """ Addition or the + operator.
        Definition: The sum of n and m is the combination of the 1's in n and m.
        It is written n + m."""
        other = other if isinstance(other, Num) else Num(other)
        return Num(self.data + other.data)

    def __sub__(self, other):
        """ Subtraction (the inverse of addition) or the - operator.
        n - m <=> The number of 1's in n that are not in m.
        """
        other = other if isinstance(other, Num) else Num(other)
        assert self.data >= other.data, f"{self.data} - {other.data} is only defined if n > m"
        return Num(self.data - other.data)

    def __mul__(self, other):
        """ * operator
        Definition: The product of numbers n and m is the string formed by a copy
        of m for every 1 in n. It is written n * m.
        """
        other = other if isinstance(other, Num) else Num(other)
        return Num(self.data * other.data)

    def __truediv__(self, other):
        """ / operator
        n / m <=> The number of times m can be subtracted from n.
        """
        other = other if isinstance(other, Num) else Num(other)
        assert self.data / other.data == self.data // other.data, \
            f"{self.data} / {other.data} is only defined if m is a factor of n"
        assert other.data != 0, "Division by zero is undefined"
        return Num(self.data // other.data)

    def __eq__(self, other):
        """ == operator
        n = m <=> The 1's in n can be paired up with the 1's in m.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data == other.data

    def __lt__(self, other):
        """ < operator
        n < m <=> n comes before m in the sequence of natural numbers.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data < other.data

    def __gt__(self, other):
        """ > operator
        n > m <=> n comes after m in the sequence of natural numbers.
        """
        other = other if isinstance(other, Num) else Num(other)
        return self.data > other.data

    def __str__(self):
        return f"N({self.data})"


class Fra:
    """
    Definition: A fraction is an ordered pair (m, n) of natural numbers, also written m / n.
    """
    def __init__(self, m, n):
        m = m if isinstance(m, Num) else Num(m)
        n = n if isinstance(n, Num) else Num(n)
        self.m = m
        self.n = n

    def __add__(self, other):
        """ Addition or the + operator.
        Definition: The sum of fractions a / b and c / d is the fraction (ad + bc) / bd.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return Fra(self.m * other.n + self.n * other.m, self.n * other.n)

    def __sub__(self, other):
        """ Subtraction or the - operator.
        Definition: The difference of fractions a / b and c / d is the fraction (ad - bc) / bd.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return Fra(self.m * other.n - self.n * other.m, self.n * other.n)

    def __mul__(self, other):
        """ Multiplication or the * operator.
        Definition: The product of fractions a / b and c / d is the fraction ac / bd.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return Fra(self.m * other.m, self.n * other.n)

    def __truediv__(self, other):
        """ Division or the / operator.
        Definition: The quotient of fractions a / b and c / d is the fraction ad / bc.
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return Fra(self.m * other.n, self.n * other.m)

    def __eq__(self, other):
        """ == operator
        (m, n) = (p, q) <=> m * q = n * p
        """
        other = other if isinstance(other, Fra) else Fra(other, 1)
        return (self.m * other.n) == (self.n * other.m)

    def __str__(self):
        return f"F({self.m.data}/{self.n.data})"


if __name__ == "__main__":
    # Natural Numbers
    a = Num(4)
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

    print("All tests passed")

    print(Num(4) + Num(2))
    print(Fra(4, 2) + Fra(2, 2))