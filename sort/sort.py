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
