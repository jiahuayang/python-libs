# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 上午8:17
# @Author  : KaWa
# @File    : clock_decorator.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

# library
# standard library
import functools
import time

# third-party library


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_list = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_list, result))
        return result
    return clocked
