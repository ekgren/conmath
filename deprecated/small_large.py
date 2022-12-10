# we can only go from zero to something


class Num:
    def __init__(self, step=0):
        if type(step) is int:
            self.step = step * "1"
        elif type(step) is Num:
            self.step = step.step

    def __repr__(self):
        return f"Num(step={len(self.step)})"

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def successor(self):
        step_new = len(self.step) + 1
        return Num(step=step_new)

    def __len__(self):
        return len(self.step)

    def __add__(self, other):
        new = Num(self)
        for _ in range(len(other)):
            new = new.successor()
        return new

    def __mul__(self, other):
        new = Num()
        store = Num(self)
        for _ in range(len(other)):
            self = self + store
        return self

    def __pow__(self, power):
        new = Num()
        for _ in range(len(power)):
            for _ in range(len(self)):
                for _ in range(len(self)):
                    new = new.successor()
        return new


class Num2:
    def __init__(self, n0=0, n1=0):
        self.n0 = Num(n0)
        self.n1 = Num(n1)

    def successor(self):
        return Num2(self.n0.successor(), self.n1)

    def predecessor(self):
        return Num2(self.n0, self.n1.successor())

    def __len__(self):
        self = self.remap()
        return len(self.n0) + len(self.n1)

    def __add__(self, other):
        for _ in range(len(other.n0)):
            self = self.successor()
        for _ in range(len(other.n1)):
            self = self.predecessor()
        return self.remap()

    def __sub__(self, other):
        for _ in range(len(other.n0)):
            self = self.successor()
        for _ in range(len(other.n1)):
            self = self.successor()
        return self

    def __mul__(self, other):
        store = Num2(self.n0, self.n1).remap()
        for _ in range(len(other.n0) - 1):
            self = self + store
        for _ in range(len(other.n1) - 1):
            self = self + store
        return self

    def __truediv__(self, other):
        store = Num2(self.n0, self.n1).remap()
        for _ in range(len(other.n0) - 1):
            self = self - store
        for _ in range(len(other.n1) - 1):
            self = self + store
        return self

    def remap(self):
        n0, n1 = self.n0, self.n1
        if n0 > n1:
            n0 = Num(len(n0.step) - len(n1.step))
            n1 = Num()
        elif n0 < n1:
            n0 = Num()
            n1 = Num(len(n1.step) - len(n0.step))
        else:
            n0 = Num()
            n1 = Num()
        return Num2(n0, n1)

    def __repr__(self):
        if self.n0 > self.n1:
            return f"{len(self.n0.step)}"
        elif self.n0 < self.n1:
            return f"-{len(self.n1.step)}"
        else:
            return "0"


print()
a = Num2(0, 6)
b = Num2(0, 3)
print(a, b)
c = a + b
print(f"{a} + {b} = {c}")
d = b + a
print(f"{b} + {a} = {d}")

a = Num2(6, 0)
b = Num2(3, 0)
print(a, b)
c = a + b
print(f"{a} + {b} = {c}")
d = b + a
print(f"{b} + {a} = {d}")

a = Num2(0, 6)
b = Num2(3, 0)
print(a, b)
c = a + b
print(f"{a} + {b} = {c}")
d = b + a
print(f"{b} + {a} = {d}")

a = Num2(6, 0)
b = Num2(0, 3)
print(a, b)
c = a + b
print(f"{a} + {b} = {c}")
d = b + a
print(f"{b} + {a} = {d}")
