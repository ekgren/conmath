class N0:
    def __init__(self):
        self.data = ""

    def successor(self):
        self.data = f"{self.data}1"
        return self

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.data):
            raise StopIteration
        else:
            self.current += 1
            return 1

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"{len(self.data)}"

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)


def add0(a, b):
    c = N0()
    for _ in a:
        c = c.successor()
    for _ in b:
        c = c.successor()
    return c


def mul0(a, b):
    c = N0()
    for _ in a:
        for _ in b:
            c = c.successor()
    return c


def make_num0(n):
    out = N0()
    for _ in range(n):
        out = out.successor()
    return out


class N1:
    def __init__(self):
        self.data = (N0(), N0())
        self.remap()

    def successor(self):
        self.data[0].successor()
        return self

    def predecessor(self):
        self.data[1].successor()
        return self

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.data):
            raise StopIteration
        else:
            self.current += 1
            return self.data[self.current - 1]

    def __repr__(self):
        if self.data[0] > self.data[1]:
            return f"{len(self.data[0])}"
        elif self.data[0] < self.data[1]:
            return f"-{len(self.data[1])}"
        else:
            return "0"

    def remap(self):
        _max = len(max(self.data))
        _min = len(min(self.data))
        new = N0()
        for _ in range(_max - _min):
            new = new.successor()
        if self.data[0] > self.data[1]:
            self.data = (new, N0())
        elif self.data[0] < self.data[1]:
            self.data = (N0(), new)
        else:
            self.data = (N0(), N0())
        return self

    @property
    def a(self):
        return self.data[0]

    @property
    def b(self):
        return self.data[1]


def make_num1(n):
    out = N1()
    if n > 0:
        for _ in range(n):
            out = out.successor()
    elif n < 0:
        for _ in range(-n):
            out = out.predecessor()
    return out


def add1(a, b):
    c = N1()
    for _ in a.a:
        c = c.successor()
    for _ in a.b:
        c = c.predecessor()
    for _ in b.a:
        c = c.successor()
    for _ in b.b:
        c = c.predecessor()
    return c.remap()


def add2(a, b):
    c = N1()
    for _ in a.a:
        c = c.predecessor()
    for _ in a.b:
        c = c.successor()
    for _ in b.a:
        c = c.predecessor()
    for _ in b.b:
        c = c.successor()
    return c.remap()


def add3(a, b):
    c = N1()
    for _ in a.a:
        c = c.successor()
    for _ in a.b:
        c = c.predecessor()
    for _ in b.a:
        c = c.predecessor()
    for _ in b.b:
        c = c.successor()
    return c.remap()


def add4(a, b):
    c = N1()
    for _ in a.a:
        c = c.predecessor()
    for _ in a.b:
        c = c.successor()
    for _ in b.a:
        c = c.successor()
    for _ in b.b:
        c = c.predecessor()
    return c.remap()


def sub1(a, b):
    c = N1()
    for _ in a.a:
        c = c.successor()
    for _ in a.b:
        c = c.predecessor()
    for _ in b.a:
        c = c.predecessor()
    for _ in b.b:
        c = c.successor()
    return c.remap()


def mul11(a, b):
    c = N1()
    for _ in a.a:
        c = add1(c, b)
    for _ in a.b:
        c = add1(c, b)
    return c.remap()


def mul12(a, b):
    c = N1()
    for _ in a.a:
        c = add1(c, b)
    for _ in a.b:
        c = add2(c, b)
    return c.remap()


def mul13(a, b):
    c = N1()
    for _ in a.a:
        c = add1(c, b)
    for _ in a.b:
        c = add3(c, b)
    return c.remap()


def mul14(a, b):
    c = N1()
    for _ in a.a:
        c = add1(c, b)
    for _ in a.b:
        c = add4(c, b)
    return c.remap()


def mul21(a, b):
    c = N1()
    for _ in a.a:
        c = add2(c, b)
    for _ in a.b:
        c = add1(c, b)
    return c.remap()


def mul22(a, b):
    c = N1()
    for _ in a.a:
        c = add2(c, b)
    for _ in a.b:
        c = add2(c, b)
    return c.remap()


def mul23(a, b):
    c = N1()
    for _ in a.a:
        c = add2(c, b)
    for _ in a.b:
        c = add3(c, b)
    return c.remap()


def mul24(a, b):
    c = N1()
    for _ in a.a:
        c = add2(c, b)
    for _ in a.b:
        c = add4(c, b)
    return c.remap()


def mul31(a, b):
    c = N1()
    for _ in a.a:
        c = add3(c, b)
    for _ in a.b:
        c = add1(c, b)
    return c.remap()


def mul32(a, b):
    c = N1()
    for _ in a.a:
        c = add3(c, b)
    for _ in a.b:
        c = add2(c, b)
    return c.remap()


def mul33(a, b):
    c = N1()
    for _ in a.a:
        c = add3(c, b)
    for _ in a.b:
        c = add3(c, b)
    return c.remap()


def mul34(a, b):
    c = N1()
    for _ in a.a:
        c = add3(c, b)
    for _ in a.b:
        c = add4(c, b)
    return c.remap()


def mul41(a, b):
    c = N1()
    for _ in a.a:
        c = add4(c, b)
    for _ in a.b:
        c = add1(c, b)
    return c.remap()


def mul42(a, b):
    c = N1()
    for _ in a.a:
        c = add4(c, b)
    for _ in a.b:
        c = add2(c, b)
    return c.remap()


def mul43(a, b):
    c = N1()
    for _ in a.a:
        c = add4(c, b)
    for _ in a.b:
        c = add3(c, b)
    return c.remap()


def mul44(a, b):
    c = N1()
    for _ in a.a:
        c = add4(c, b)
    for _ in a.b:
        c = add4(c, b)
    return c.remap()


n = N1()

a = make_num1(3)
b = make_num1(-2)
c = add1(a, b)
print(f"{a} +(1) {b} = {c}")
e = add2(a, b)
print(f"{a} +(2) {b} = {e}")
c = add3(a, b)
print(f"{a} +(3) {b} = {c}")
e = add4(a, b)
print(f"{a} +(4) {b} = {e}")

print()
d = mul11(a, b)
print(f"{a} *(11) {b} = {d}")
d = mul12(a, b)
print(f"{a} *(12) {b} = {d}")
d = mul13(a, b)
print(f"{a} *(13) {b} = {d}")
d = mul14(a, b)
print(f"{a} *(14) {b} = {d}")

print()
d = mul31(a, b)
print(f"{a} *(31) {b} = {d}")
d = mul32(a, b)
print(f"{a} *(32) {b} = {d}")
d = mul33(a, b)
print(f"{a} *(33) {b} = {d}")
d = mul34(a, b)
print(f"{a} *(34) {b} = {d}")

print()
d = mul21(a, b)
print(f"{a} *(21) {b} = {d}")
d = mul22(a, b)
print(f"{a} *(22) {b} = {d}")
d = mul23(a, b)
print(f"{a} *(23) {b} = {d}")
d = mul24(a, b)
print(f"{a} *(24) {b} = {d}")

print()
d = mul41(a, b)
print(f"{a} *(41) {b} = {d}")
d = mul42(a, b)
print(f"{a} *(42) {b} = {d}")
d = mul43(a, b)
print(f"{a} *(43) {b} = {d}")
d = mul44(a, b)
print(f"{a} *(44) {b} = {d}")
