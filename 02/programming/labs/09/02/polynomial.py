"""Polynomial."""


class Polynomial:
    """Polynomial."""

    def __init__(self, degree=None, coefficient=None):
        """Receives info."""
        if degree is None:
            self._poly_head = None
        else:
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    def degree(self):
        """Degree."""
        if self._poly_head is None:
            return -1
        else:
            return self._poly_head.degree

    def __getitem__(self, degree):
        """Gets item."""
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree != degree:
            cur_node = cur_node.next
        if cur_node is None or cur_node.degree != degree:
            return 0.0
        else:
            return cur_node.coefficient

    def evaluate(self, scalar):
        """Evaluates."""
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None:
            result += cur_node.coefficient * (scalar**cur_node.degree)
            cur_node = cur_node.next
        return result

    def __add__(self, rhs_poly):
        """Adds."""
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()
        i = max_degree
        while i >= 0:
            value = self[i] + rhs_poly[i]
            new_poly.append_term(i, value)
            i -= 1
        return new_poly

    def __sub__(self, rhs_poly):
        """Substracts."""
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            value = self[i] - rhs_poly[i]
            new_poly.append_term(i, value)
            i -= 1
        return new_poly

    def __mul__(self, rhs_poly):
        """Multiplies."""
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()
        i = max_degree
        while i >= 0:
            temp = max_degree
            while temp >= 0:
                value = self[i] * rhs_poly[temp]
                new_poly.append_term(i + temp, value)
                temp -= 1
            i -= 1
        return new_poly

    def simple_add(self, rhs_poly):
        """Simple add."""
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()
        i = max_degree
        while i >= 0:
            value = self[i] + rhs_poly[i]
            new_poly.append_term(i, value)
            i -= 1
        return new_poly

    def append_term(self, degree, coefficient):
        """Appends term."""
        if coefficient != 0.0:
            new_term = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    def __str__(self):
        """Short info."""
        probe = self._poly_head
        res = ""
        while probe is not None:
            if str(probe)[0] != "-":
                text = "+" + str(probe)
            else:
                text = str(probe)
            res += f"{text}"
            probe = probe.next
        return res


class _PolyTermNode(object):
    """PolyTermNode."""

    def __init__(self, degree, coefficient):
        """Receives info."""
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """Prints the value stored in self."""
        return str(self.coefficient) + "x" + str(self.degree)
