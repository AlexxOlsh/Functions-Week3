import unittest
from functools import reduce


def process_numbers(numbers):
    numbers = list(filter(lambda x: x > 0, numbers))
    print(f'Filter: {numbers}')
    numbers = list(map(lambda x: x**2, numbers))
    print(f'Map: {numbers}')
    res = reduce(lambda x, y: int(x) + int(y), numbers)
    return res


def test_process_numbers():
    assert process_numbers([1, 2, 3, 4, 5, -2, -4]) == 20


unittest.main()