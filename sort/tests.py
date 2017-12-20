# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:58
# @Author  : KaWa
# @File    : tests.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

from sort import *

if __name__ == "__main__":
    """test bubble sort
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
    """

    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)