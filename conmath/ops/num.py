from conmath.containers import Num


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
    for _ in enumerator:
        item = successor(item)
    return item


def mul(item, enumerator):
    b = Num()
    for _ in enumerator:
        b = add(b, item)
    return b


def eq(a: Num, b: Num) -> bool:
    """Check if two Num are equal."""
    return a.data == b.data


def test():
    a = Num(2)
    b = Num(3)
    c = add(a, b)
    d = mul(a, b)
    print(c)
    print(d)


if __name__ == "__main__":
    test()
