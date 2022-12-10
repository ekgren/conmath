class Contain:
    def __init__(self, *args):
        self.args = args
        self.cdepth = 0
        self.ctype = "C"
        if len(self) > 0:
            if isinstance(self.args[0], Contain):
                ctype = self.args[0].ctype
                assert all(
                    e.ctype == ctype for e in self.args
                ), "All elements must be of the same type."
                self.cdepth = self.args[0].cdepth + 1
                self.ctype += f"({','.join([e.ctype for e in self.args])})"
            elif isinstance(self.args[0], type(None)):
                assert all(
                    e is None for e in self.args
                ), "All elements must be of the same type."
            else:
                raise TypeError("All elements must be Contain objects.")

    def __repr__(self):
        return f"Contain({', '.join(repr(e) for e in self.args)})"

    def __len__(self):
        return len(self.args)

    def __getitem__(self, key):
        return self.args[key]

    def __iter__(self):
        return iter(self.args)


def make_num(a: int):
    assert a >= 0, "Cannot make negative numbers."
    return Contain(*[None for _ in range(a)])


def make_int(a: int):
    if a < 0:
        return Contain(make_num(0), make_num(-a))
    else:
        return Contain(make_num(a), make_num(0))


def make_fra(a: int, b: int):
    return Contain(make_num(a), make_num(b))


def make_rat(a: int, b: int):
    return Contain(make_int(a), make_int(b))


def add(a, b):
    return Contain(*a, *b)


def mul(a, b):
    c = Contain()
    for _ in b:
        c = add(c, a)
    return c


a = make_int(2)
b = make_int(-3)
print(a)
print(b)
print()

ops_add = {}
ops_mul = {}
for x in a:
    for y in b:
        ops_add[(x, y)] = add(x, y)

n = []
for v in ops_add.values():
    for vv in ops_add.values():
        n = Contain(v, vv)
        print(len(n[0]) - len(n[1]))
