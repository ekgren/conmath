from .types import Rat


def lies_on(line, point):
    """ Checks if a line lies on the point.
    Definition: A line <a:b:c> lies on a rational point [x, y] <=> a * x + b * y = c.
    """
    assert isinstance(line, Line), "Line must be a Line object."
    assert isinstance(point, Point), "Point must be a Point object."

    x, y = point.a, point.b
    a, b, c = line.a, line.b, line.c
    return (a * x + b * y + c) == 0


# The basic framework for geometry (I) | Arithmetic and Geometry Math Foundations 23 | N J Wildberger
# Link: https://youtu.be/8rkrymhphMQ
class Point:
    """
    Definition: A rational point is an ordered pair [a, b] of rational numbers.
    """
    def __init__(self, a, b):
        a = a if isinstance(a, Rat) else Rat(a)
        b = b if isinstance(b, Rat) else Rat(b)
        self.a = a
        self.b = b


# The basic framework for geometry (I) | Arithmetic and Geometry Math Foundations 23 | N J Wildberger
# Link: https://youtu.be/8rkrymhphMQ
class Line:
    """
    Definition: A line is an ordered proportion <a:b:c> of rational numbers in which a and b are not both zero.
    """
    def __init__(self, a, b, c):
        a = a if isinstance(a, Rat) else Rat(a)
        b = b if isinstance(b, Rat) else Rat(b)
        c = c if isinstance(c, Rat) else Rat(c)
        self.a = a
        self.b = b
        self.c = c

    def __contains__(self, point):
        return lies_on(line=self, point=point)
