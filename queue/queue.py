# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:31
# @Author  : KaWa
# @File    : queue.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

# library
# standard library

# third-party library


class Queue:
    def __init__(self):
        self._list = []

    def enqueue(self, item):
        """append an item to queue"""
        self._list.append(item)

    def dequeue(self):
        """queue delete an item"""
        return self._list.pop(0)

    def is_empyt(self):
        """the queue is empty or not"""
        return not self._list

    def size(self):
        """return the number item of queue"""
        return len(self._list)