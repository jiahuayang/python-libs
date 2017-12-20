# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:02
# @Author  : KaWa
# @File    : stack.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

"""""""""""
A module to implement the stack
"""""""""""

# library
# standard library

# third-party library


class Stack:
    def __init__(self):
        self._list = []

    def push(self, item):
        """push item to the stack"""
        self._list.append(item)

    def pop(self):
        """stack pop a item"""
        self._list.pop()

    def peek(self):
        """return the top item of the stack"""
        if self._list:
            return self._list[-1]
        else:
            return None

    def is_empty(self):
        """stack is empty or not"""
        return not self._list          # or return self._list == []

    def size(self):
        """return the item number of the stack"""
        return len(self._list)
