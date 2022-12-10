from data_types import C0, C1, C2


def add_c0(a, b):
    assert type(a) == type(b), "a and b must be the same type"
    instance_type = type(a)
    return instance_type(*a, *b)


def main():
    a = C1(C0(None))
    print(a)
    b = C1(C0(None))
    print(b)
    c = add_c0(a, b)
    print(c)


if __name__ == "__main__":
    main()
