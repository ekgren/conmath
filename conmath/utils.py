from typing import Any
from inspect import signature
from containers import Num
from operations import successor_num


def arity(func: Any) -> int:
    """Returns the arity of a function.
    Arity is the number of arguments or operands taken by a function, operation or relation in logic, mathematics, and
    computer science. In mathematics, arity may also be named rank, but this word can have many other meanings in
    mathematics. In logic and philosophy, it is also called adicity and degree. In linguistics, it is usually named
    valency.
    https://en.wikipedia.org/wiki/Arity"""
    assert callable(func), "function must be callable"
    return len(signature(func).parameters)


def make_num(n: int) -> Num:
    """Returns a Num object with the given value."""
    x = Num()
    for _ in range(n):
        x = successor_num(x)
    return x
