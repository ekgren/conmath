from __future__ import annotations

from conmath.operations import unary_operation, binary_operation
from conmath.relations import binary_relation


class Num:
    """
    The Num type is a type of natural numbers.
    """

    def __init__(self, data=None):
        if data is None:
            self.data = ""
        elif type(data) is str:
            self.data = data
        elif type(data) is int:
            assert data >= 0, "data must be >= 0"
            self.data = "1" * data
        elif type(data) is Num:
            self.data = data.data
        else:
            raise TypeError(f"Cannot initialize Num with {type(data)}.")

    ##############################
    # Relations defined on the Num type
    ##############################
    @binary_relation
    def eq(a: Num, b: Num) -> bool:
        """Check if two Num are equal."""
        return a.data == b.data

    ##############################
    # Operations defined on the Num type
    ##############################
    @unary_operation
    def successor(a: Num) -> Num:
        """Returns the successor of a Num."""
        return Num(f"{a.data}1")

    @binary_operation
    def combine(a: Num, b: Num) -> Num:
        """Combine two Num."""
        c = Num()
        for _ in a:
            c = Num.successor(c)
        for _ in b:
            c = Num.successor(c)
        return c

    @binary_operation
    def add(item, enumerator):
        """Add one Num to another Num."""
        for _ in enumerator:
            item = Num.successor(item)
        return item

    @binary_operation
    def mul(item, enumerator):
        """Multiply one Num by another Num."""
        b = Num()
        for _ in enumerator:
            b = Num.add(b, item)
        return b

    @binary_operation
    def div(numerator, denominator):
        """
        Discussion will refer to the form N / D = (Q,R), where

        N = numerator (dividend)
        D = denominator (divisor)
        is the input, and

        Q = quotient
        R = remainder
        is the output.

        The simplest division algorithm, historically incorporated into a greatest common divisor algorithm presented in
        Euclid's Elements, Book VII, Proposition 1, finds the remainder given two positive integers using only subtractions
        and comparisons:

        R := N
        Q := 0
        while R ≥ D do
          R := R − D
          Q := Q + 1
        end
        return (Q,R)
        """

        quotient = Num()
        remainder = numerator
        while remainder >= denominator:
            remainder = remainder - denominator
            quotient = Num.successor(quotient)
        return quotient, remainder

    ##############################
    # Python methods
    ##############################
    def __add__(self, other):
        return Num.add(self, other)

    def __sub__(self, other):
        return Num.sub(self, other)

    def __mul__(self, other):
        return Num.mul(self, other)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"{len(self.data)}"

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self):
            raise StopIteration
        else:
            self.current += 1
            return 1


def test():
    a = Num(2)
    b = Num(0)
    c = Num.add(a, b)
    d = Num.mul(a, b)
    print(c)
    print(d)


if __name__ == "__main__":
    test()
