# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午10:00
# @Author  : KaWa
# @File    : tests.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

from search import *


if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 55))
    print(binary_search(li, 100))
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 100))
