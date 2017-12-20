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
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
