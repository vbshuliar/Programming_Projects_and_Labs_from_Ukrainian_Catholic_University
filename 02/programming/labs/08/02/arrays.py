"""Arrays."""
import ctypes


class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size

        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration


class Array2D:
    def __init__(self, num_rows, num_cols):

        self.rows = Array(num_rows)

        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        return len(self.rows)

    def num_cols(self):
        return len(self.rows[0])

    def clear(self, value):
        for row in range(self.num_rows()):
            row.clear(value)

    def __getitem__(self, index_tuple):
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert (
            0 <= row < self.num_rows() and 0 <= col < self.num_cols()
        ), "Array subscript out of range."
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert (
            0 <= row < self.num_rows() and 0 <= col < self.num_cols()
        ), "Array subscript out of range."
        array_1d = self.rows[row]
        array_1d[col] = value


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    @staticmethod
    def _make_array(c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""

        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value( or  raise ValueError)."""

        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1

                return
        raise ValueError("value not found")
