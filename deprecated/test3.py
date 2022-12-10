N = 3

####################
# Helper functions
####################


def info(a):
    print(int(len(a) / N))


# This is considered cheating
def _num(i):
    assert isinstance(i, int), f"{i} must be an integer"
    assert i >= 0, f"{i} must be a positive integer"
    # return i * ((),)
    a = num()
    for _ in range(i):
        a = S(a)
    return a


####################
# Math
####################


def num(*args):
    return args


def S(a):  # Successor function
    return num(*a, *[num() for i in range(N)])


def P(a):
    return a[:-N]


def add(a, b):
    c = num()
    for _ in a[::N]:
        c = S(c)
    for _ in b[::N]:
        c = S(c)
    return c


def sub(a, b):
    for _ in b[::N]:
        a = P(a)
    return a


def mul(a, b):
    c = num()
    for _ in range(len(a[::N]) * len(b[::N])):
        c = S(c)
    return c


def div(a, b):
    c = num()
    d = num(*b)
    while len(d) <= len(a):
        c = S(c)
        d = add(d, b)
    return c


def _add(a, b):
    return a + b


def _mul(a, b):
    return a * len(b)


def _sub(a, b):
    return a[: -len(b)]


def eq(a, b):
    if len(a) == len(b):
        return True
    else:
        return False


zero = num()
s = S(zero)
ss = S(s)
sss = S(ss)

info(zero)
info(s)
info(ss)
info(sss)
print(20 * "=")
a = _num(3)
b = _num(2)
c = div(a, b)
d = mul(c, b)
info(a)
info(b)
info(c)
info(d)
print(eq(a, d))
