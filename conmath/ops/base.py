def over(a, b, c, function):
    """For each element in a apply binary function to c and b."""
    for _ in a:
        c = function(c, b)
    return c

