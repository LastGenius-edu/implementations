"""
# Implements the Array ADT using array capabilities of the ctypes module.
"""
import ctypes


class Array:
    """
    Creates an array with size elements.
    """
    def __init__(self, size):
        """
        Initializer
        :param size: int
        """
        assert size > 0, "Array size must be > 0"
        self._size = size

        # Create the array structure using the ctypes module.
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()

        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.
        :return: int
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the contents of the index element.
        :param index: int
        :return: item
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        :param index: int
        :param value: value
        :return: None
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        """
        Clears the array by setting each element to the given value.
        :param value: value
        :return: None
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.
        :return:
        """
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    """
    An iterator for the Array ADT.
    """
    def __init__(self, the_array):
        """
        Initializer
        :param the_array: Array
        """
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
    """
    Implementation of the Array2D ADT using an array of arrays.
    """
    def __init__(self, num_rows, num_cols):
        """
        Creates a 2D array of size numRows x numCols.
        :param num_rows: int
        :param num_cols: int
        """
        # Create a 1D array to store an array reference for each row.
        self.rows = Array(num_rows)

        # Create the 1D arrays for each row of the 2D array.
        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the 2 -D array.
        :return: int
        """
        return len(self.rows)

    def num_cols(self):
        """
        Returns the number of columns in the 2 -D array.
        :return: int
        """
        return len(self.rows[0])

    def clear(self, value):
        """
        Clears the array by setting every element to the given value.
        :param value: value
        :return: None
        """
        for row in self.rows:
            row.clear(value)

    def __getitem__(self, index_tuple):
        """
        Gets the contents of the element at position [i, j]
        :param index_tuple: (int, int)
        :return: value
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), "Array subscript out of range."
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """
        Sets the contents of the element at position [i,j] to value.
        :param index_tuple: (int, int)
        :param value: value
        :return: None
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), "Array subscript out of range."
        array_1d = self.rows[row]
        array_1d[col] = value


class DynamicArray:
    """
    A dynamic array class akin to a simplified Python list.
    """
    def __init__(self):
        """
        Create an empty array.
        """
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def _make_array(self, c):  # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self.n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value( or  raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item

                return  # exit immediately
        raise ValueError("value not found")  # only reached if no match
