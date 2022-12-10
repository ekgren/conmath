""" Factory for building functions from strings.
Plan is to use this for automatically exploring the space of functions."""

template = """
def {}({}):
    {}
"""

exec(template.format("test", "a, b, c", "print(a, b, c)"))
test(1, 2, 3)
