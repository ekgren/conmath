from __future__ import annotations

from conmath.contypes import Num
from conmath.operations import unary_operation, binary_operation
from conmath.relations import binary_relation


class NumBi:
    def __init__(self, data=None):
        if data is None:
            data = (Num(), Num())
        elif type(data) is NumBi:
            data = data.data

        assert type(data) == tuple, "Data must be a tuple."
        assert len(data) == 2, "Data must be a tuple of length 2."
        x, y = data[0], data[1]
        assert type(x) is type(y), "Both elements must be of the same type."
        if isinstance(x, Num):
            self.data = data
        elif isinstance(x, int):
            self.data = (Num(x), Num(y))
        else:
            raise TypeError(f"Cannot initialize NumBi with {type(data)}.")

    ##############################
    # Relations defined on the NumBi type
    ##############################
    @binary_relation
    def eq(a: NumBi, b: NumBi) -> bool:
        """Check if two NumBi are equal."""
        return Num.eq(a.x, b.x) and Num.eq(a.y, b.y)

    ##############################
    # Operations defined on the NumBi type
    ##############################
    @unary_operation
    def successor_x(a: NumBi) -> NumBi:
        """Returns the successor of NumBi x."""
        data = (Num.successor(a.x), a.y)
        return NumBi(data)

    @unary_operation
    def successor_y(a: NumBi) -> NumBi:
        """Returns the successor of NumBi y."""
        data = (a.x, Num.successor(a.y))
        return NumBi(data)

    # It's starting to get hairy here already.
    # Should write a function to generate these.
    # Hardest part will be a reasonable naming scheme.
    @binary_operation
    def add_xyxy(a: NumBi, b: NumBi) -> NumBi:
        """Add two NumBi."""
        c = NumBi()
        for _ in a.x:
            c = NumBi.successor_x(c)
        for _ in a.y:
            c = NumBi.successor_y(c)
        for _ in b.x:
            c = NumBi.successor_x(c)
        for _ in b.y:
            c = NumBi.successor_y(c)
        return c

    @binary_operation
    def add_xxyy(a: NumBi, b: NumBi) -> NumBi:
        """Add two NumBi."""
        c = NumBi()
        for _ in a.x:
            c = NumBi.successor_x(c)
        for _ in a.y:
            c = NumBi.successor_x(c)
        for _ in b.x:
            c = NumBi.successor_y(c)
        for _ in b.y:
            c = NumBi.successor_y(c)
        return c

    @binary_operation
    def add_yxyx(a: NumBi, b: NumBi) -> NumBi:
        """Add two NumBi."""
        c = NumBi()
        for _ in a.x:
            c = NumBi.successor_y(c)
        for _ in a.y:
            c = NumBi.successor_x(c)
        for _ in b.x:
            c = NumBi.successor_y(c)
        for _ in b.y:
            c = NumBi.successor_x(c)
        return c

    @binary_operation
    def add_yyxx(a: NumBi, b: NumBi) -> NumBi:
        """Add two NumBi."""
        c = NumBi()
        for _ in a.x:
            c = NumBi.successor_y(c)
        for _ in a.y:
            c = NumBi.successor_y(c)
        for _ in b.x:
            c = NumBi.successor_x(c)
        for _ in b.y:
            c = NumBi.successor_x(c)
        return c

    @binary_operation
    def add_yxxy(a: NumBi, b: NumBi) -> NumBi:
        """Add two NumBi."""
        c = NumBi()
        for _ in a.x:
            c = NumBi.successor_y(c)
        for _ in a.y:
            c = NumBi.successor_x(c)
        for _ in b.x:
            c = NumBi.successor_x(c)
        for _ in b.y:
            c = NumBi.successor_y(c)
        return c

    @binary_operation
    def add_xyyx(a: NumBi, b: NumBi) -> NumBi:
        """Add two NumBi."""
        c = NumBi()
        for _ in a.x:
            c = NumBi.successor_x(c)
        for _ in a.y:
            c = NumBi.successor_y(c)
        for _ in b.x:
            c = NumBi.successor_y(c)
        for _ in b.y:
            c = NumBi.successor_x(c)
        return c

    def __len__(self):
        raise NotImplementedError("Cannot get length of NumBi.")

    def __repr__(self):
        return f"{self.data}"

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]


def test():
    a = Num(5)
    print(a)

    b = NumBi()
    print(b)


if __name__ == "__main__":
    test()
