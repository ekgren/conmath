from number import Number


class Field:
    """ A field is a set on which the operations of multiplication, addition, subtraction and division
    are defined and satisfy certain basic rules. The most common examples of fields are given by the
    integers mod p when p is a prime number. When mod is not prime, there are elements other than
    zero that are not invertible.

    TODO: Figure out how to do rational numbers.
    FOR NOW ONLY DO MODULAR ARITHMETIC!
    """
    def __init__(self, type='rational', mod=None):
        assert isinstance(type, str), f"type = {type} needs to be str"
        assert type in ['rational', 'mod'], f"type = {type} needs to be in ['rational', 'mod']"
        self.type = type
        if type == 'mod':
            assert isinstance(mod, int), f"mod = {mod} needs to be int"
        self.mod = mod

    def add(self, a, b):
        """ + operator """
        assert isinstance(a, Number), f"a = {a} needs to be Number"
        b = b if isinstance(b, Number) else Number(b, field=self)
        assert a.field == b.field, f"Numbers must belong to the same field: a({a.field}) b({b.field})"

        if type == 'rational':
            #TODO: Figure out how to do rational numbers.
            data = a.data + b.data
        elif type == 'mod':
            data = (a.data + b.data) % self.mod

        return Number(data, field=self)

    def mul(self, a, b):
        """ * operator """
        assert isinstance(a, Number), f"a = {a} needs to be Number"
        b = b if isinstance(b, Number) else Number(b, field=self)
        assert a.field == b.field, f"Numbers must belong to the same field: a({a.field}) b({b.field})"

        if type == 'rational':
            # TODO: Figure out how to do rational numbers.
            data = a.data * b.data
        elif type == 'mod':
            data = (a.data * b.data) % self.mod

        return Number(data, field=self)

    def pow(self, a, b):
        """ ** operator """
        assert isinstance(b, int), "only supporting int powers for now"

        if type == 'rational':
            # TODO: Figure out how to do rational numbers.
            data = a ** b
        elif type == 'mod':
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
        return f"Field(type={self.type}, mod={self.mod})"

    def __str__(self):
        return f"Field(type={self.type}, mod={self.mod})"
