#!/usr/bin/env python3
import bisect
import random


# Insert as a sorted array. Search O(log n) BUT insert is O(n)
def sorted_array_bisect(array):
    result = []
    for i, value in array:
        bisect.insort(result, value)
    return result


# Create new array, sort that. Append is O(1) and sorted is O(n log n)
def sorted_array(array):
    result = []
    for i, value in array:
        result.append(value)
    result = sorted(result)
    return result


def create_array(length):
    max_value = 42 ** 2
    for i in range(length):
        yield (1, random.randint(0, max_value))


if __name__ == "__main__":
    array = list(create_array(8))
    print(f"{array}")
    sorted_bisect = sorted_array_bisect(array)
    sorted_sorted = sorted_array(array)
    assert sorted_bisect == sorted_sorted
    print(sorted_sorted)
