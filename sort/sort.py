# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:55
# @Author  : KaWa
# @File    : bubble_sort.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

def bubble_sort(alist):
    """bubble sort"""
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return


def select_sort(alist):
    """select sort"""
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(min_index+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[min_index], alist[j] = alist[j], alist[min_index]


def insert_sort(alist):
    """insert sort"""
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


def shell_sort(alist):
    """shell sort"""
    n = len(alist)
    gap = n // 2
    # i = gap
    # for i in range(gap, n):
    #     # i = [gap, gap+1, gap+2, gap+3... n-1]
    #     while:
    #     if alist[i] < alist[i-gap]:
    #         alist[i], alist[i-gap] = alist[i-gap], alist[i]

    while gap > 0:
        for j in range(gap, n):
            # j = [gap, gap+1, gap+2, gap+3, ..., n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # reduce gap
        gap //= 2


def quick_sort(alist, first, last):
    """quick sort"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high shift left
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        # left shift right
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    # exit the while loop, high equal low,
    # don't forget to put back the mid_value
    alist[low] = mid_value

    # left of the low
    quick_sort(alist, first, low-1)
    # right of the low
    quick_sort(alist, low+1, last)


def merge_sort(alist):
    """merge sort"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # merge(left, right)
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <=  right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result