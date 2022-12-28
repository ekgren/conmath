"""
https://en.wikipedia.org/wiki/Binary_relation

In mathematics, a binary relation associates instances of one type, called the domain, with instances of another type,
called the codomain. A binary relation over type X and Y is a new type of ordered pairs (x, y) consisting of instance
x of X and y of Y.
"""


class Relation(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        return self.func


def relation(func):
    return Relation(func)


# TODO: Is this a thing???
class UnaryRelation(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        return self.func


def unary_relation(func):
    return UnaryRelation(func)


class BinaryRelation(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        return self.func


def binary_relation(func):
    return BinaryRelation(func)
