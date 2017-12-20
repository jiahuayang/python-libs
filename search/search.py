# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午9:57
# @Author  : KaWa
# @File    : search.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

# library
# standard library

# third-party library


def binary_search(alist, item):
    """binary search, "alist" must be ordered, implement by recursion"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search_2(alist, item):
    """binary search, implement not by recursion"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first+last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False