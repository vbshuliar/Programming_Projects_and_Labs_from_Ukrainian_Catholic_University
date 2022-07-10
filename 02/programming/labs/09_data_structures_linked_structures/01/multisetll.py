"""Multiset."""

from node import Node


class Multiset:
    """Multiset."""

    def __init__(self):
        """Receives information."""
        self._head = None

    def empty(self):
        """Checks emptiness of Multiset."""
        return self._head == None

    def __contains__(self, value):
        """Checks existence of value in the Multiset."""
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """Adds."""
        if self._head is None:
            self._head = Node(value)
        else:
            new = Node(value)
            new.next = self._head
            self._head = new

    def delete(self, value):
        """Delets."""
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """Removes everything."""
        output = []
        while self._head is not None:
            output.append(self._head.item)
            self.delete(self._head.item)
        return output

    def split_half(self):
        """Splits."""
        if self._head.next is None:
            return
        length, multi1, multi2, probe = len(self), Multiset(), Multiset(), self._head
        for _ in range(length):
            if _ < length / 2:
                multi1.reverse_add(probe.item)
            else:
                multi2.reverse_add(probe.item)
            probe = probe.next
        return multi1, multi2

    def __len__(self):
        """Len of the multiset."""
        counter, probe = 0, self._head
        while probe is not None:
            probe = probe.next
            counter += 1
        return counter

    def reverse_add(self, value):
        """Reversed addition."""
        new = Node(value)
        if self._head is None:
            self._head = new
        else:
            probe = self._head
            while probe.next is not None:
                probe = probe.next
            probe.next = new

    def extend(self, multi):
        """Extends."""
        new = Multiset()
        probe = multi._head
        while probe is not None:
            new.reverse_add(probe.item)
            probe = probe.next
        probe = self._head
        while probe is not None:
            new.reverse_add(probe.item)
            probe = probe.next
        return new
