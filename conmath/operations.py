"""
https://en.wikipedia.org/wiki/Operation_(mathematics)

Notes:
We have two types of operations (functions) an extension type and a counting type.
- The extension family of functions operate directly on the container.
  An example of the extension family of functions is the successor function.
- The counting family of functions performs an operation and counts how many times that operation is performed.
  An example of that is division.
"""


class Operation(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        return self.func


def operation(func):
    return Operation(func)


class UnaryOperation(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        return self.func


def unary_operation(func):
    return UnaryOperation(func)


class BinaryOperation(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        return self.func


def binary_operation(func):
    return BinaryOperation(func)
