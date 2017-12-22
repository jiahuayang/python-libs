# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 上午10:43
# @Author  : KaWa
# @File    : series.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

# library
# standard library

# third-party library


def factorial(n):
    """factorial series, 'n' is natural number"""
    return n if n<2 else n*factorial(n-1)


