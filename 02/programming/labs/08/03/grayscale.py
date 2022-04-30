"""Image."""

import numpy as np
from PIL import Image, ImageOps
from io import StringIO
import ctypes


class GrayscaleImage:
    """Grayscale image class."""

    def __init__(self, nrows, ncols):
        """Receives information."""
        self.user_photo = np.zeros((nrows, ncols))

    def __repr__(self):
        """Brief info about class object."""
        return f"{self.user_photo}"

    def width(self):
        """Width."""
        return len(self.user_photo[0])

    def height(self):
        """Length."""
        return len(self.user_photo)

    def clear(self, value):
        """Clears the image."""
        if value in range(0, 256):
            for row in range(len(self.user_photo)):
                for col in range(len(self.user_photo[row])):
                    self.user_photo[row][col] = value
        else:
            raise ValueError("Value must be in range from 0 to 255.")

    def getitem(self, row, col):
        """Returns the value of the wanted pixel."""
        if row in range(0, self.height()) and col in range(0, self.width()):
            return self.user_photo[row][col]
        else:
            raise ValueError("Value must be in correct range.")

    def setitem(self, row, col, value):
        """Sets new value for the wanted pixel."""
        if row in range(0, self.height()) and col in range(0, self.width()):
            self.user_photo[row][col] = value
        else:
            raise ValueError("Value must be in correct range.")

    def from_file(self, path):
        """Creates object from image."""
        self.user_photo = np.array(ImageOps.grayscale(Image.open(path)))

    def lzw_compression(self):
        """Compresses data with LZW algorithm."""
        size = 256
        data = dict((chr(_), _) for _ in range(size))
        text = ""
        for number in np.ravel(self.user_photo):
            text += chr(number)
        num = ""
        output = []
        for el in text:
            _ = num + el
            if _ in data:
                num = _
            else:
                output.append(data[num])
                data[_] = size
                size += 1
                num = el
        output.append(data[num]) if num else ""
        output = (
            np.array(output, dtype="uint32")
            if max(output) > 2**16
            else np.array(output, dtype="uint16")
        )
        self.compressed = output
        return output

    def lzw_decompression(self):
        """Decompresses data with LZW algorithm."""
        size = 256
        data = dict((_, chr(_)) for _ in range(size))
        output = StringIO()
        compressed = list(self.compressed)
        el = chr(compressed.pop(0))
        output.write(el)
        for _ in compressed:
            if _ in data:
                var = data[_]
            elif _ == size:
                var = el + el[0]
            else:
                raise ValueError("Bad compressed k: %s" % _)
            output.write(var)
            data[size] = el + var[0]
            size += 1
            el = var
        output = output.getvalue()
        data = dict((chr(_), _) for _ in range(size))
        text = ""
        for elem in output:
            text += str(data[elem]) + " "
        return np.array([int(_) for _ in text.strip().split()], dtype="uint8").reshape(
            (self.height(), self.width())
        )


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


if __name__ == "__main__":
    # test = GrayscaleImage(100, 40)
    # print("Array:\n", test.user_photo)
    # print("Width:\n", test.width())
    # print("Height:\n", test.height())
    # test.clear(228)
    # print("New array:\n", test.user_photo)
    # test.setitem(0, 0, 77)
    # print("Updated array:\n", test.user_photo)
    # print("Get item:\n(0, 0):", test.getitem(0, 0))

    # print("____________________")

    # path = r"02/labs/08/03/test.png"
    # test = GrayscaleImage(*ImageOps.grayscale(Image.open(path)).size[::-1])
    # test.from_file(path)
    # print("Array:\n", test.user_photo)
    # print("Width:\n", test.width())
    # print("Height:\n", test.height())
    # print("Decompressed after compression and initial array comparison:")
    # test.lzw_compression()
    # decompressed = test.lzw_decompression()
    # print(test.user_photo == decompressed)

    # test = Image.fromarray(decompressed)
    # test.show()

    a = Array2D(100, 150)
    print(a.num_cols())
    print(a.num_rows())
    
