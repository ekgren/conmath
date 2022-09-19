from field import Field


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
        return f"Number(data={self.data}, field={self.field})"

    def __str__(self):
        return f"Number(data={self.data}, field={self.field})"

    def item(self):
        return self.data
