from collections import namedtuple


class Machine0:
    def __init__(self):
        self.ix = 0
        self.write = None
        self.halt = False

    def step(self, tape):
        data = tape[self.ix]
        if data == "_":
            if self.write is None:
                tape = self.do_write(tape)
                self.do_move("r")
            else:
                self.halt = True
        elif data == "0":
            self.write = "1"
            tape = self.do_write(tape)
            self.do_move("r")
        elif data == "1":
            self.write = "0"
            tape = self.do_write(tape)
            self.do_move("r")
        return tape

    def do_write(self, tape):
        if self.write is None:
            return tape
        else:
            pre = tape[: self.ix]
            post = tape[self.ix + 1 :]
            return pre + self.write + post

    def do_move(self, move):
        if move is None:
            pass
        elif move == "l":
            self.ix -= 1
        elif move == "r":
            self.ix += 1


m = Machine0()
tape = "_01000101011100100101001_"
print(tape)
while m.halt is False:
    tape = m.step(tape)
print(tape)
