from containers import Num, NumBi


def successor_num(x: Num) -> Num:
    """Returns the successor of a Num."""
    x.data = f"{x.data}1"
    return x


def eq_num(x: Num, y: Num) -> bool:
    """Check if two Num are equal."""
    return x.data == y.data


def add_num(x: Num, y: Num) -> Num:
    """Add two Num."""
    z = Num()
    for _ in x:
        z = successor_num(z)
    for _ in y:
        z = successor_num(z)
    return z


def mul_num(x: Num, y: Num) -> Num:
    """Multiply two Num."""
    z = Num()
    for _ in x:
        z = add_num(z, y)
    return z


def eq_num_bi(x: NumBi, y: NumBi) -> bool:
    """Check if two NumBi are equal."""
    return eq_num(x.data[0], y.data[0]) and eq_num(x.data[1], y.data[1])
