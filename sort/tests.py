# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:58
# @Author  : KaWa
# @File    : tests.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

from sort import *

if __name__ == "__main__":
    """test bubble sort
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
    """

    """test select sort
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
    """

    """test insert sort
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)
    """

    """test shell sort
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)
    """

    """test quick sort
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
    """

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)