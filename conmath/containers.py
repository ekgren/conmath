class Num:
    def __init__(self, data=None):
        if data is None:
            self.data = ""
        elif type(data) is str:
            self.data = data
        elif type(data) is int:
            assert data >= 0, "data must be >= 0"
            self.data = "1" * data
        elif type(data) is Num:
            self.data = data.data
        else:
            raise TypeError(f"Cannot initialize Num with {type(data)}.")

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"{len(self.data)}"

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self):
            raise StopIteration
        else:
            self.current += 1
            return 1


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
