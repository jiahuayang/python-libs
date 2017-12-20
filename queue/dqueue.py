# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:38
# @Author  : KaWa
# @File    : dqueue.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.


class Dqueue:
    """double side queue"""
    def __init__(self):
        self._list = []

    def add_front(self, item):
        """add item to the front of the double queue"""
        self._list.insert(0, item)

    def add_rear(self, item):
        """add item to the rear of the double queue"""
        self._list.append(item)

    def pop_front(self):
        """pop item to the front of the double queue"""
        return self._list.pop(0)

    def pop_rear(self):
        """pop item to the rear of the double queue"""
        return self._list.pop()

    def is_empty(self):
        """the double queue is empty or not"""
        return not self._list

    def size(self):
        """return the number item of the double queue"""
        return len(self._list)