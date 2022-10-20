""" A property of an operation is a truth statement of the inputs to the operation. """
from utils import arity
from operations import add_num


def commutative(binary_operation, a, b) -> bool:
    """In mathematics, a binary operation is commutative if changing the order of the operands does not change the
    result. It is a fundamental property of many binary operations, and many mathematical proofs depend on it.

    The name is needed because there are operations, such as division and subtraction, that do not have it
    (for example, "3 − 5 ≠ 5 − 3"); such operations are not commutative, and so are referred to as noncommutative
    operations. The idea that simple operations, such as the multiplication and addition of numbers, are commutative
    was for many years implicitly assumed.

    A corresponding property exists for binary relations; a binary relation is said to be symmetric if the relation
    applies regardless of the order of its operands; for example, equality is symmetric as two equal mathematical
    objects are equal regardless of their order.

    https://en.wikipedia.org/wiki/Commutative_property"""
    assert arity(binary_operation) == 2, "binary_operation must take two arguments"
    assert type(a) == type(b), "a and b must be of the same type"
    return binary_operation(a, b) == binary_operation(b, a)


def associative(binary_operation, a, b, c) -> bool:
    """In mathematics, an operation is associative if changing the grouping of its operands does not change the
    result. For example, the addition of three numbers is associative, because the result is the same regardless of
    how the numbers are grouped. For example, (a + b) + c = a + (b + c). The associative property is a fundamental
    property of many binary operations, and many mathematical proofs depend on it. The name is needed because there
    are operations, such as division and subtraction, that do not have it (for example, "(a − b) − c ≠ a − (b − c)").
    The idea that simple operations, such as the multiplication and addition of numbers, are associative was for
    many years implicitly assumed. Thus, this property was not named until the 19th century, when mathematics started
    to become formalized.

    https://en.wikipedia.org/wiki/Associative_property"""
    assert arity(binary_operation) == 2, "binary_operation must take two arguments"
    assert type(a) == type(b) == type(c), "a, b, and c must be of the same type"
    left = binary_operation(a, binary_operation(b, c))
    right = binary_operation(binary_operation(a, b), c)
    return left == right


def left_distributive(binary_operation_a, binary_operation_b, a, b, c) -> bool:
    """In mathematics, a binary operation is said to be left-distributive over another binary operation if the
    following equation holds:

    a * (b + c) = (a * b) + (a * c)
    b + c = d
    a * b = e
    a * c = f
    a * d = e + f

    where a, b, and c are elements of the same type, and * and + are binary operations. The operation + is said to be
    distributive over the operation *.

    https://en.wikipedia.org/wiki/Distributive_property"""
    assert arity(binary_operation_a) == 2, "binary_operations must take two arguments"
    assert arity(binary_operation_b) == 2, "binary_operations must take two arguments"
    assert type(a) == type(b) == type(c), "a, b, and c must be of the same type"

    d = binary_operation_b(b, c)
    left = binary_operation_a(a, d)

    e = binary_operation_a(a, b)
    f = binary_operation_a(a, c)
    right = binary_operation_b(e, f)
    return left == right


def right_distributive(binary_operation_a, binary_operation_b, a, b, c) -> bool:
    """In mathematics, a binary operation is said to be right-distributive over another binary operation if the
    following equation holds:

    (b + c) * a = (b * a) + (c * a)
    b + c = d
    b * a = e
    c * a = f
    d * a = e + f

    where a, b, and c are elements with the same type, and * and + are binary operations. The operation + is said to be
    distributive over the operation *.

    https://en.wikipedia.org/wiki/Distributive_property"""
    assert arity(binary_operation_a) == 2, "binary_operations must take two arguments"
    assert arity(binary_operation_b) == 2, "binary_operations must take two arguments"
    assert type(a) == type(b) == type(c), "a, b, and c must be of the same type"
    d = binary_operation_b(b, c)
    left = binary_operation_a(d, a)

    e = binary_operation_a(b, a)
    f = binary_operation_a(c, a)
    right = binary_operation_b(e, f)
    return left == right


def distributive(binary_operation_a, binary_operation_b, a, b, c) -> bool:
    """In mathematics, a binary operation is said to be distributive over another binary operation if the
    following equation holds:

    (b + c) * a = (b * a) + (c * a)

    where a, b, and c are elements of the same type, and * and + are binary operations. The operation + is said to be
    distributive over the operation *.

    https://en.wikipedia.org/wiki/Distributive_property"""
    assert arity(binary_operation_a) == 2, "binary_operations must take two arguments"
    assert arity(binary_operation_b) == 2, "binary_operations must take two arguments"
    assert type(a) == type(b) == type(c), "a, b, and c must be of the same type"
    left_distributivity = left_distributive(
        a, b, c, binary_operation_a, binary_operation_b
    )
    right_distributivity = right_distributive(
        a, b, c, binary_operation_a, binary_operation_b
    )
    return left_distributivity and right_distributivity


if __name__ == "__main__":
    a = 1
    b = 2
    commutativity = commutative(add_num, a, b)
    print(f"commutativity between {a} and {b}: {commutativity}")
