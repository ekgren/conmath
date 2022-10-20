############################################################
# Addition operations
############################################################


def add_num(a, b):
    """Addition or the + operator.
    Definition: The sum of m and n is the combination of the 1's in m and n.
    It is written m + n."""
    assert type(a) == type(b), "a and b must be the same type"
    instance_type = type(a)
    m = a.data
    n = b.data
    return instance_type(m + n)


def add_int(a, b):
    """Addition or the + operator.
    Definition: The sum of integers m | n and k | l is the integer (m + k) | (n + l).
    """
    assert type(a) == type(b), "a and b must be the same type"
    assert len(a.data) == 2 and len(b.data) == 2, "a and b must be of the form (m, n)"
    instance_type = type(a)
    m = a.data[0]
    n = a.data[1]
    k = b.data[0]
    l = b.data[1]
    return instance_type(add_num(m, k), add_num(n, l))


def add_frac(a, b):
    """Addition or the + operator.
    Definition: The sum of fractions m / n and k / l is the fraction (ml + nk) / nl.
    """
    assert type(a) == type(b), "a and b must be the same type"
    instance_type = type(a)
    m = a.data[0]
    n = a.data[1]
    k = b.data[0]
    l = b.data[1]
    ml = mul_num(m, l)
    nk = mul_num(n, k)
    nl = mul_num(n, l)
    ml_add_nk = add_num(ml, nk)
    return instance_type(ml_add_nk, nl)


############################################################
# Subtraction functions
############################################################


def sub_num(a, b):
    """Subtraction (the inverse of addition) or the - operator.
    n - m <=> The number of 1's in n that are not in m.
    """
    assert type(a) == type(b), "a and b must be the same type"
    instance_type = type(a)
    data_a = a.data
    data_b = b.data
    return instance_type(data_a - data_b)


def sub_int(a, b):
    """Subtraction or the - operator.
    Definition: The difference of integers m | n and k | l is the integer (m + l) | (n + k).
    """
    assert type(a) == type(b), "a and b must be the same type"
    assert len(a.data) == 2 and len(b.data) == 2, "a and b must be of the form (m, n)"
    instance_type = type(a)
    m = a.data[0]
    n = a.data[1]
    k = b.data[0]
    l = b.data[1]
    return instance_type(add_num(m, l), add_num(n, k))


############################################################
# Multiplication functions
############################################################


def mul_num(a, b):
    """* operator
    Definition: The product of numbers n and m is the string formed by a copy
    of m for every 1 in n. It is written n * m.
    """
    assert type(a) == type(b), "a and b must be the same type"
    instance_type = type(a)
    data_a = a.data
    data_b = b.data
    return instance_type(data_a * data_b)


def mul_int(a, b):
    """Multiplication or the * operator.
    Definition: The product of integers m | n and k | l is the integer (mk + nl) | (ml + nk).
    """
    assert type(a) == type(b), "a and b must be the same type"
    assert len(a.data) == 2 and len(b.data) == 2, "a and b must be of the form (m, n)"
    instance_type = type(a)
    m = a.data[0]
    n = a.data[1]
    k = b.data[0]
    l = b.data[1]
    mk = mul_num(m, k)
    nl = mul_num(n, l)
    ml = mul_num(m, l)
    nk = mul_num(n, k)
    mk_add_nl = add_num(mk, nl)
    ml_add_nk = add_num(ml, nk)
    return instance_type(mk_add_nl, ml_add_nk)


############################################################
# Division functions
############################################################


def div_num(a, b):
    """/ operator
    m / n <=> The number of times n can be subtracted from m.
    """
    assert type(a) == type(b), "a and b must be the same type"
    instance_type = type(a)
    m = a.data
    n = b.data
    assert n != 0, "Cannot divide by zero"
    return instance_type(m / n)
