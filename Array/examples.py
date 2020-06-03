# Fill a 1-D array with random values, then print the values.
import array
import random
import sys

from arrays import Array


def main():
    """
    Main func
    """
    # The constructor is called to create the array.
    value_list = Array(1)

    # Fill the array with random floating-point values.
    for i in range(len(value_list)):
        value_list[i] = random.random()
    # Print the values, one per line.
    for i in range(len(value_list)):
        print(value_list[i])
    for i in value_list:
        print(i)

    # get size of list
    data = []
    for i in range(15):
        a = len(data)
        b = sys.getsizeof(data)
        print(" Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
        data.append(None)


if __name__ == '__main__':
    main()
