from conmath.containers import NumBi
import conmath.ops.num as num


def eq(a: NumBi, b: NumBi) -> bool:
    """Check if two NumBi are equal."""
    return num.eq(a.x, b.x) and num.eq(a.y, b.y)


def successor_x(a: NumBi) -> NumBi:
    """Returns the successor of NumBi x."""
    data = (num.successor(a.x), a.y)
    return NumBi(data)


def successor_y(a: NumBi) -> NumBi:
    """Returns the successor of NumBi y."""
    data = (a.x, num.successor(a.y))
    return NumBi(data)


# It's starting to get hairy here already.
# Should write a function to generate these.
# Hardest part will be a reasonable naming scheme.
def add_xyxy(a: NumBi, b: NumBi) -> NumBi:
    """Add two NumBi."""
    c = NumBi()
    for _ in a.x:
        c = successor_x(c)
    for _ in a.y:
        c = successor_y(c)
    for _ in b.x:
        c = successor_x(c)
    for _ in b.y:
        c = successor_y(c)
    return c


def add_xxyy(a: NumBi, b: NumBi) -> NumBi:
    """Add two NumBi."""
    c = NumBi()
    for _ in a.x:
        c = successor_x(c)
    for _ in a.y:
        c = successor_x(c)
    for _ in b.x:
        c = successor_y(c)
    for _ in b.y:
        c = successor_y(c)
    return c


def add_yxyx(a: NumBi, b: NumBi) -> NumBi:
    """Add two NumBi."""
    c = NumBi()
    for _ in a.x:
        c = successor_y(c)
    for _ in a.y:
        c = successor_x(c)
    for _ in b.x:
        c = successor_y(c)
    for _ in b.y:
        c = successor_x(c)
    return c


def add_yyxx(a: NumBi, b: NumBi) -> NumBi:
    """Add two NumBi."""
    c = NumBi()
    for _ in a.x:
        c = successor_y(c)
    for _ in a.y:
        c = successor_y(c)
    for _ in b.x:
        c = successor_x(c)
    for _ in b.y:
        c = successor_x(c)
    return c


def add_yxxy(a: NumBi, b: NumBi) -> NumBi:
    """Add two NumBi."""
    c = NumBi()
    for _ in a.x:
        c = successor_y(c)
    for _ in a.y:
        c = successor_x(c)
    for _ in b.x:
        c = successor_x(c)
    for _ in b.y:
        c = successor_y(c)
    return c


def add_xyyx(a: NumBi, b: NumBi) -> NumBi:
    """Add two NumBi."""
    c = NumBi()
    for _ in a.x:
        c = successor_x(c)
    for _ in a.y:
        c = successor_y(c)
    for _ in b.x:
        c = successor_y(c)
    for _ in b.y:
        c = successor_x(c)
    return c
