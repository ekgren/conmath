from conmath.containers import Num


def successor(a: Num) -> Num:
    """Returns the successor of a Num."""
    return Num(f"{a.data}1")


def eq(a: Num, b: Num) -> bool:
    """Check if two Num are equal."""
    return a.data == b.data


def add(a: Num, b: Num) -> Num:
    """Add two Num."""
    c = Num()
    for _ in a:
        c = successor(c)
    for _ in b:
        c = successor(c)
    return c


def mul(a: Num, b: Num) -> Num:
    """Multiply two Num."""
    c = Num()
    for _ in a:
        c = add(c, b)
    return c
