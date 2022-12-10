from operations import add_num, sub_num, mul_num, div_num
from properties import commutative, associative

############################################################
# The laws of arithmetic
############################################################


def laws_of_addition(a, b, c):
    """The laws of addition are:
    commutativity: a + b = b + a
    associativity: (a + b) + c = a + (b + c)
    """
    assert type(a) == type(b) == type(c), "a, b, and c must be of the same type"
    instance_type = type(a)
    commutativity = commutative(instance_type.add, a, b)
    associativity = associative(instance_type.add, a, b, c)
    return commutativity and associativity


def laws_of_multiplication(a, b, c):
    """The laws of multiplication are:
    commutativity: a * b = b * a
    associativity: (a * b) * c = a * (b * c)
    identity: a * 1 = 1 * a = a
    """
    commutativity = commutative(mul_num, a, b)
    associativity = associative(mul_num, a, b, c)
    identity = a * 1 == 1 * a == a
    return commutativity and associativity and identity


def laws_of_subtraction(a, b, c):
    """The laws of subtraction are:"""

    def law_one(a, b, c):
        return a - (b + c) == (a - b) - c

    def law_two(a, b):
        return a + (b - c) == (a + b) - c

    def law_three(a, b):
        return a - (b - c) == (a - b) + c

    return law_one(a, b, c) and law_two(a, b) and law_three(a, b)


def laws_of_division(a, b, c):
    """The laws of division are:"""

    def law_one(a, b):
        return a / b + c / b == (a + c) / b

    def law_two(a, b):
        return (b * a) / (b * c) == a / c

    return law_one(a, b) and law_two(a, b)


def distributive_law(a, b, c):
    """a * (b + c) = (a * b) + (a * c)     (Distributive)"""
    return a * (b + c) == (a * b) + (a * c) and (a + b) * c == (a * c) + (b * c)
