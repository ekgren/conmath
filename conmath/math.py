class Field:
    """
    Formally, a field is a set F together with two binary operations on F called addition and multiplication.
    A binary operation on F is a mapping F × F → F, that is, a correspondence that associates with each ordered
    pair of elements of F a uniquely determined element of F. The result of the addition of a and b is
    called the sum of a and b, and is denoted a + b. Similarly, the result of the multiplication of a and b is
    called the product of a and b, and is denoted ab or a ⋅ b. These operations are required to satisfy the
    following properties, referred to as field axioms (in these axioms, a, b, and c are arbitrary elements of
    the field F):

    Associativity of addition and multiplication:
        a + (b + c) = (a + b) + c, and a ⋅ (b ⋅ c) = (a ⋅ b) ⋅ c.
    Commutativity of addition and multiplication:
        a + b = b + a, and a ⋅ b = b ⋅ a.
    Additive and multiplicative identity:
        there exist two different elements 0 and 1 in F such that a + 0 = a and a ⋅ 1 = a.
    Additive inverses:
        for every a in F, there exists an element in F, denoted −a, called the additive inverse of a,
        such that a + (−a) = 0.
    Multiplicative inverses:
        for every a ≠ 0 in F, there exists an element in F, denoted by a−1 or 1/a, called the multiplicative
        inverse of a, such that a ⋅ a−1 = 1.
    Distributivity of multiplication over addition:
        a ⋅ (b + c) = (a ⋅ b) + (a ⋅ c).

    This may be summarized by saying:
        a field has two operations, called addition and multiplication; it is an abelian group under addition
        with 0 as the additive identity; the nonzero elements are an abelian group under multiplication with
        1 as the multiplicative identity; and multiplication distributes over addition.

    Even more summarized:
        a field is a commutative ring where 0 != 1 and all nonzero elements are invertible.


    TODO: Figure out how to do rational numbers. FOR NOW ONLY DO MODULAR ARITHMETIC!
    """
    def __init__(self, type='rational', mod=None):
        assert isinstance(type, str), f"type = {type} needs to be str"
        assert type in ['rational', 'mod'], f"type = {type} needs to be in ['rational', 'mod']"
        self.type = type
        if type == 'mod':
            assert isinstance(mod, int), f"mod = {mod} needs to be a positive int"
            assert mod > 0, f"mod = {mod} needs to be a positive int"
        self.mod = mod

    def add(self, a, b):
        """ + operator """
        assert isinstance(a, Number), f"a = {a} needs to be Number"
        b = b if isinstance(b, Number) else Number(b, field=self)
        assert a.field == b.field, f"Numbers must belong to the same field: a({a.field}) b({b.field})"

        if self.type == 'rational':
            #TODO: Figure out how to do rational numbers.
            data = a.data + b.data
        elif self.type == 'mod':
            data = (a.data + b.data) % self.mod
        else:
            raise NotImplementedError

        return Number(data, field=self)

    def mul(self, a, b):
        """ * operator """
        assert isinstance(a, Number), f"a = {a} needs to be Number"
        b = b if isinstance(b, Number) else Number(b, field=self)
        assert a.field == b.field, f"Numbers must belong to the same field: a({a.field}) b({b.field})"

        if self.type == 'rational':
            # TODO: Figure out how to do rational numbers.
            data = a.data * b.data
        elif self.type == 'mod':
            data = (a.data * b.data) % self.mod

        return Number(data, field=self)

    def pow(self, a, b):
        """ ** operator """
        assert isinstance(b, int), "only supporting int powers for now"

        if self.type == 'rational':
            # TODO: Figure out how to do rational numbers.
            data = a ** b
        elif self.type == 'mod':
            if b < 0:
                data = (a ** (self.mod - 2)) % self.mod  # If self.mod is prime
                data = (data ** abs(b)) % self.mod
            elif b == 0:
                data = 1
            elif b > 0:
                data = (a ** b) % self.mod

        return Number(data, field=self)

    def number(self, data):
        return Number(data, field=self)

    def __eq__(self, other):
        return self.type == other.type and self.mod == other.mod

    def __repr__(self):
        return f"F({self.type}, {self.mod})"

    def __str__(self):
        return f"F({self.type}, {self.mod})"


class Number:
    """ A number object have data and an associated field. The field is a set on which the operations of
    multiplication, addition, subtraction and division are defined and satisfy certain basic rules. """
    def __init__(self, data, field):
        assert isinstance(data, int), f"data = {data} needs to be int"
        assert isinstance(field, Field), f"field = {field} needs to be a Field"
        self.data = data
        self.field = field

    def __add__(self, other):
        """ + operator """
        other = other if isinstance(other, Number) else Number(other, field=self.field)
        return self.field.add(self, other)

    def __mul__(self, other):
        """ * operator """
        other = other if isinstance(other, Number) else Number(other, field=self.field)
        return self.field.mul(self, other)

    def __pow__(self, other):
        """ ** operator """
        assert isinstance(other, (int, Number)), "only supporting int powers for now"
        return self.field.pow(self, other)

    def __neg__(self):  # -self
        return self * -1

    def __radd__(self, other):  # other + self
        return self + other

    def __sub__(self, other):  # self - other
        return self + (-other)

    def __rsub__(self, other):  # other - self
        return other + (-self)

    def __rmul__(self, other):  # other * self
        return self * other

    def __truediv__(self, other):  # self / other
        return self * other ** -1

    def __rtruediv__(self, other):  # other / self
        return other * self ** -1

    def __repr__(self):
        return f"N({self.data}) ∈ {self.field}"

    def __str__(self):
        return f"N({self.data}) ∈ {self.field}"

    def __eq__(self, other):
        return self.data == other.data and self.field == other.field

    def item(self):
        return self.data


class Point:
    """ A point object have x and y coordinates that belong to an associated field. """
    def __init__(self, x, y):
        assert isinstance(x, Number), f"x = {x} needs to be Number"
        assert isinstance(y, Number), f"y = {y} needs to be Number"
        assert x.field == y.field, f"Points must belong to the same field: x({x.field}) y({y.field})"
        self.x = x
        self.y = y
        self.field = x.field

    def __add__(self, other):
        """ + operator """
        assert isinstance(other, Point), f"other = {other} needs to be Point"
        assert self.field == other.field, f"Points must belong to the same field: self({self.field}) other({other.field})"
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """ * operator """
        raise NotImplementedError

    def __repr__(self):
        return f"P({self.x.data}, {self.y.data}) ∈ {self.field}"



if __name__ == '__main__':

    F = Field(type='mod', mod=7)
    a = F.number(2)
    b = F.number(3)
    print(a, b)
    print(a + b)

    p = Point(a, b)
    print(p)
