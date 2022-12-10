""" https://en.wikipedia.org/wiki/Algebraic_structure """

# TODO: Should reimplement with a focus on type (set) and operations (add, mul, etc.)
def field(a, b, c):
    """A field is a set of numbers that satisfies the following properties:"""

    def closure(a, b):
        """Closure under addition and multiplication"""
        return True  # type(a + b) == type(a) and type(a * b) == type(a)

    def commutative(a, b):
        """Commutative"""
        return a + b == b + a and a * b == b * a

    def associative(a, b, c):
        """Associative"""
        return (a + b) + c == a + (b + c) and (a * b) * c == a * (b * c)

    def identity(a):
        """Identity"""
        return a + 0 == a and a * 1 == a

    def inverse(a):
        """Inverse"""
        return a + (-a) == 0 and a * (1 / a) == 1

    def distributive(a, b, c):
        """Distributive"""
        return a * (b + c) == (a * b) + (a * c) and (a + b) * c == (a * c) + (b * c)

    return (
        closure(a, b)
        and commutative(a, b)
        and associative(a, b, c)
        and identity(a)
        and inverse(a)
        and distributive(a, b, c)
    )
