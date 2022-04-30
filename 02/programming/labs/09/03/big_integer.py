"""Big integer."""
VARIANT = 72


class BigInteger:
    """ADT Big Integer."""

    def __init__(self, initValue="0"):
        """Receives information."""
        self.positive = initValue[0] != "-"

        if not self.positive:
            self._head = TwoWayNode(initValue[1])
            start = 2
        else:
            self._head = TwoWayNode(initValue[0])
            start = 1

        self._tail = self._head

        for _ in initValue[start:]:
            self._tail.after = TwoWayNode(_, self._tail)
            self._tail = self._tail.after

    def to_string(self):
        """Returns number."""
        return str(self)

    def __repr__(self):
        """Prints number."""
        res = ""
        head = self._head

        while head:
            res += head.data
            head = head.after

        return "-" + res if not self.positive else res

    def __ne__(self, rhsint):
        """Not equal."""
        if not (self.positive and rhsint.positive):
            return True

        head_1 = self._head
        head_2 = rhsint._head

        while head_1 or head_2:
            if head_1.data != head_2.data:
                return True

            head_1 = head_1.after
            head_2 = head_2.after

        return False

    def __lt__(self, rhsint):
        """Less."""
        if not self.positive and rhsint.positive:
            return True

        if self.positive and not rhsint.positive:
            return False

        head_1 = self._head
        head_2 = rhsint._head

        while head_1 or head_2:
            if head_1 is None:
                return True
            if head_2 is None:
                return False
            head_1 = head_1.after
            head_2 = head_2.after

        head_1 = self._head
        head_2 = rhsint._head

        while head_1 or head_2:
            if int(head_1.data) < int(head_2.data):
                return True
            if int(head_1.data) > int(head_2.data):
                return False
            head_1 = head_1.after
            head_2 = head_2.after

        return False

    def __add__(self, rhsint):
        """Adds."""
        return BigInteger(self.add_help(rhsint))

    def add_help(self, rhsint):
        """Add helper."""
        big, small = self.bigger_smaller(rhsint)

        if self.positive and not rhsint.positive:

            if self == big:
                return self.simple_sub(rhsint)

            if self == small:
                return "-" + rhsint.simple_sub(self)

        if not self.positive and rhsint.positive:

            if self == big:
                return "-" + self.simple_sub(rhsint)

            if self == small:
                return rhsint.simple_sub(self)

        if not self.positive and not rhsint.positive:
            return "-" + self.simple_add(rhsint)

        return self.simple_add(rhsint)

    def simple_add(self, rhsint):
        """Simple add."""
        big, small = self.bigger_smaller(rhsint)
        big_tail = big._tail
        small_tail = small._tail
        result = ""
        extra = 0

        while big_tail:
            bigger = int(big_tail.data)
            smaller = int(small_tail.data) if small_tail else 0
            temp = bigger + smaller + extra
            extra = temp // 10
            temp = temp % 10
            result += str(temp)
            big_tail = big_tail.previous
            small_tail = small_tail.previous if small_tail else 0

        if extra > 0:
            result += str(extra)

        return self.cut_zeros(result[::-1])

    def __sub__(self, rhsint):
        """Substracts."""
        return BigInteger(self.sub_help(rhsint))

    def sub_help(self, rhsint):
        """Sub helper."""
        big, small = self.bigger_smaller(rhsint)

        if self.positive and rhsint.positive:

            if self == small:
                return "-" + rhsint.simple_sub(self)

        if self.positive and not rhsint.positive:
            return self.simple_add(rhsint)

        if not self.positive and rhsint.positive:

            if self == big:
                return "-" + self.simple_add(rhsint)

            if self == small:
                return "-" + rhsint.simple_sub(self)

        if not self.positive and not rhsint.positive:

            if self == big:
                return "-" + self.simple_sub(rhsint)

            if self == small:
                return rhsint.simple_sub(self)

        return self.simple_sub(rhsint)

    def simple_sub(self, rhsint):
        """Simple sub."""
        big, small = self.bigger_smaller(rhsint)
        big_tail = big._tail
        small_tail = small._tail
        result = ""
        extra = 0

        while big_tail:

            bigger = int(big_tail.data)
            smaller = int(small_tail.data) if small_tail else 0

            temp = bigger - smaller - extra

            if temp < 0:
                temp += 10
                extra = 1

            else:
                extra = 0

            result += str(temp)
            big_tail = big_tail.previous
            small_tail = small_tail.previous if small_tail else 0

        return self.cut_zeros(result[::-1])

    def __mul__(self, rhsint):
        """Multiplies."""
        return BigInteger(self.mul_help(rhsint))

    def mul_help(self, rhsint):
        """Multiply helper."""
        if (self.positive and not rhsint.positive) or (
            not self.positive and rhsint.positive
        ):
            return "-" + str(self.simple_mul(rhsint))

        return str(self.simple_mul(rhsint))

    def simple_mul(self, rhsint):
        """Simple multiply."""
        big, small = self.bigger_smaller(rhsint)
        big_tail = big._tail
        small_tail = small._tail
        result = BigInteger()
        extra = 0
        counter = 0

        while small_tail:

            temp_num = big_tail
            temp_result = ""
            smaller = int(small_tail.data)

            while temp_num:

                bigger = int(temp_num.data)

                temp = bigger * smaller + extra
                extra = temp // 10
                temp = temp % 10

                temp_result += str(temp)

                try:
                    temp_num = temp_num.previous

                except AttributeError:
                    temp_num = False

            if extra > 0:
                temp_result += str(extra)
                extra = 0

            temp_result = temp_result[::-1] + "0" * counter
            counter += 1

            try:
                temp_result_1 = BigInteger(temp_result)
                result = result + temp_result_1
                small_tail = small_tail.previous

            except AttributeError:
                small_tail = False

        return result

    def __floordiv__(self, rhsint):
        """Floor division."""
        return BigInteger(self.floordiv_help(rhsint))

    def floordiv_help(self, rhsint):
        """Floor division helper."""
        big, small = self.bigger_smaller(rhsint)

        if (self.positive and not rhsint.positive) or (
            not self.positive and rhsint.positive
        ):

            if self == big:

                counter = 1
                temp = rhsint

                while self == big:
                    temp += rhsint
                    counter += 1
                    big, small = self.bigger_smaller(temp)

                return "-" + str(counter)

            if self == small:
                return "-1"

        temp = self
        counter = 0
        big, small = temp.bigger_smaller(rhsint)

        while temp == big:
            temp -= rhsint
            counter += 1
            big, small = temp.bigger_smaller(rhsint)

        return str(counter)

    def __mod__(self, rhsint):
        """Modulo."""
        return BigInteger(str(self - (rhsint * (self // rhsint))))

    def __pow__(self, rhsint):
        """Power."""
        return BigInteger(self.pow_help(rhsint))

    def pow_help(self, rhsint):
        """Power helper."""
        if not self.positive and rhsint.positive:

            if rhsint.convert_to_int() % 2 != 0:
                return str(self.simple_pow(rhsint))

        return str(self.simple_pow(rhsint))

    def simple_pow(self, rhsint):
        """Simple power."""
        temp = self

        if rhsint.convert_to_int() == 0:
            return "1"

        for _ in range(rhsint.convert_to_int() - 1):
            temp *= self

        return temp

    def __rshift__(self, rhsint):
        """Right shift."""
        return BigInteger(
            str(bin((self // BigInteger("2") ** rhsint).convert_to_int())[2:])
        )

    def __or__(self, rhsint):
        """Or."""
        big, small = self.bigger_smaller(rhsint)
        big = str(bin(big.convert_to_int())[2:])
        small = str(bin(small.convert_to_int())[2:]).zfill(len(big))
        result = ""

        for _ in range(len(big)):
            result += str(int(big[_]) | int(small[_]))

        return BigInteger(result)

    def bigger_smaller(self, rhsint):
        """Compares numbers."""
        head_1 = self._head
        head_2 = rhsint._head

        while head_1 or head_2:

            if head_1 is None:
                return rhsint, self

            if head_2 is None:
                return self, rhsint

            head_1 = head_1.after
            head_2 = head_2.after

        head_1 = self._head
        head_2 = rhsint._head

        while head_1 or head_2:

            if int(head_1.data) < int(head_2.data):
                return rhsint, self

            if int(head_1.data) > int(head_2.data):
                return self, rhsint

            head_1 = head_1.after
            head_2 = head_2.after

        return self, rhsint

    def cut_zeros(self, text):
        """Cuts unnecessary zeros."""
        while text[0] == "0" and len(text) > 1:
            text = text[1:]

        return text

    def convert_to_int(self):
        """Converts to num."""
        result = ""
        head = self._head

        while head:
            result += head.data
            head = head.after

        return int(result)


class TwoWayNode:
    """Two way node."""

    def __init__(self, data, previous=None, after=None):
        """Receives information."""
        self.data = data
        self.after = after
        self.previous = previous
