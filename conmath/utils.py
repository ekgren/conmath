from typing import Any
from inspect import signature


def arity(func: Any) -> int:
    """Returns the arity of a function.
    Arity is the number of arguments or operands taken by a function, operation or relation in logic, mathematics, and
    computer science. In mathematics, arity may also be named rank, but this word can have many other meanings in
    mathematics. In logic and philosophy, it is also called adicity and degree. In linguistics, it is usually named
    valency.
    https://en.wikipedia.org/wiki/Arity"""
    assert callable(func), "function must be callable"
    return len(signature(func).parameters)


# We might want to add something like arity for the number of elements in type data tuples.

# For later if we want to build a graph on what functions use what functions we can use this:
# https://stackoverflow.com/questions/51901676/get-the-lists-of-functions-used-called-within-a-function-in-python
