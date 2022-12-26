from conmath.containers import Num


docstring = """
We have two classes of functions an extension type and an counting type.
- The extension family of functions operate directly on the container.
  An example of the extension family of functions is the successor function.
- The counting family of functions performs an operation and counts how many times that operation is performed.
  An example of that is division.
"""


def successor(a: Num) -> Num:
    """Returns the successor of a Num."""
    return Num(f"{a.data}1")


def combine(a: Num, b: Num) -> Num:
    """Combine two Num."""
    c = Num()
    for _ in a:
        c = successor(c)
    for _ in b:
        c = successor(c)
    return c


def add(item, enumerator):
    """Add one Num to another Num."""
    for _ in enumerator:
        item = successor(item)
    return item


def mul(item, enumerator):
    """Multiply one Num by another Num."""
    b = Num()
    for _ in enumerator:
        b = add(b, item)
    return b


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
        quotient = successor(quotient)
    return quotient, remainder


def eq(a: Num, b: Num) -> bool:
    """Check if two Num are equal."""
    return a.data == b.data


def test():
    a = Num(2)
    b = Num(0)
    c = add(a, b)
    d = mul(a, b)
    print(c)
    print(d)


if __name__ == "__main__":
    test()
