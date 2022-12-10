############################################################
# Type implementations
############################################################


def info(a):
    print(len(a), a)


def hierarchical_parser(a):
    """Function that recursively parses nested tuples as a
    tree and return the number of children at each node."""
    if type(a) == tuple:
        return (len(a),) + tuple(hierarchical_parser(e) for e in a if len(e) > 0)
    else:
        return tuple()


def make_num(a: int) -> tuple:
    assert a >= 0, "a must be a positive integer"
    return contain(*[contain() for _ in range(a)])


def make_int(a: int) -> tuple:
    if a < 0:
        return contain(contain(), make_num(-a))
    else:
        return contain(make_num(a), contain())


def make_fra(a: int, b: int = 1) -> tuple:
    return contain(make_num(a), make_num(b))


def make_rat(a: int, b: int = 1) -> tuple:
    return contain(make_int(a), make_int(b))


# We start with four operations
# unpack, for, contain


def contain(*args):
    return (*args,)


def successor(args):
    return contain(*args, contain())


def add(a, b):
    """
    Addition can be defined with either unpack or successor.
    for _ in b:
        a = successor(a)
    """
    return contain(*a, *b)


def mul(a, b):
    c = contain()
    for _ in b:
        c = add(c, a)
    return c


def sub(a, b):
    return a[len(b) :]


def div(a, b):
    if len(b) == 0:
        print("Warning: division by zero computation will not terminate ;)")
    c = contain()
    while len(a) >= len(b):
        a = sub(a, b)
        c = successor(c)
    return c


def add2(a, b):
    # Addition of integers m | n and k | l is the integer (m + k) | (n + l).
    # But also generalised to more dims
    c = contain()
    for (d, e) in zip(a, b):
        c = contain(*c, add(d, e))
    return c


def mul2(a, b):
    # Definition: The product of integers m | n and k | l is the integer (mk + nl) | (ml + nk).
    # Not sure how to generalise this to more dims
    c = add(mul(a[0], b[0]), mul(a[1], b[1]))
    d = add(mul(a[0], b[1]), mul(a[1], b[0]))
    return contain(c, d)


def sub2(a, b):
    # Definition: The difference of integers m | n and k | l is the integer (m + l) | (n + k).
    # Not sure how to generalise this to more dims
    c = add(a[0], b[1])
    d = add(a[1], b[0])
    return contain(c, d)


def div2(a, b):
    return None


def main():
    class Contain(tuple):
        def __new__(cls, *args):
            return super().__new__(cls, args)

        def __init__(self, *args, ctype="Contain"):
            assert sum(1 for e in args if type(e) == ctype) == len(
                args
            ), "All elements must be Contain objects."
            self._args = args

        def __repr__(self):
            return f"Contain{super().__repr__()}"

    a = Contain(Contain(), Contain(Contain(), Contain()))
    info(a)


if __name__ == "__main__":
    main()
