"""Angle adt."""


class AngleADT:
    """Angle ADT."""

    def encode_message(self, message):
        """Encodes the message."""
        result = []
        last = 0
        for _ in message:
            for num in self.char_to_numbers(_):
                num *= 22.5
                if num - last != 0:
                    result.append(num - last)
                else:
                    result.append(360.0)
                last = num
        return result

    def char_to_numbers(self, character):
        """Converts character to number."""
        result = []
        for _ in hex(ord(character))[2:]:
            result.append(int(_, 16))
        return result
