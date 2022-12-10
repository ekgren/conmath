class Num:
    def __init__(self):
        self.data = ""

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
    def __init__(self):
        self.data = (Num(), Num())

    def __len__(self):
        raise NotImplementedError("Cannot get length of NumBi.")

    def __repr__(self):
        return f"{self.data}"


if __name__ == "__main__":
    a = NumBi()
    print(a)
