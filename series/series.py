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
    """ factorial series, 'n' is natural number
    0! = 1
    1! = 1
    2! = 2*1
    3! = 3*2*1 """

    return n if n<2 else n*factorial(n-1)


def fibonacci(n):
    """ fibonacci series, 'n' is natural number
    fibonacci(0)=0
    fibonacci(1)=1
    fibonacci(2)=fibonacci(1)+fibonacci(0)=1
    fibonacci(3)=fibonacci(2)+fibonacci(1)+fibonacci(0)=2"""

    return n if n<2 else fibonacci(n-1) + fibonacci(n-2)
