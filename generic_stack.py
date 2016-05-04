#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random


def quick_sort(array):
    _partition(array, 0, len(array)-1)


def _partition(array, left, right):
    i, j = left, right
    pivot = array[(left + right) / 2]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            if i != j:  # Avoid swapping same index
                array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if left < j:
        _partition(array, left, j)

    if i < right:
        _partition(array, i, right)


def shuffle(array):
    for i in range(len(array)):
        r = random.randint(0, len(array)-1)
        if r != i:
            array[i], array[r] = array[r], array[i]


# list has to be sorted before calling the function
def remove_duplicates(array):
    result = [None for i in array]
    k = 0

    for i in range(len(array)):
        if k == 0:
            result[k] = array[i]
            k += 1
        else:
            if array[i] == result[k-1]:
                continue
            else:
                result[k] = array[i]
                k += 1

    return result[0:k]


def main():
    l = [2, 2, 3, 5, 84, 9, 9, 35, 21, 214, 74]
    print "Intial stack: %s" % str(l)
    shuffle(l)
    print "Shuffled stack: %s" % str(l)
    quick_sort(l)
    print "Sorted stack: %s" % str(l)
    print "Stack without duplicates: %s" % str(remove_duplicates(l))


if __name__ == "__main__":
    main()
