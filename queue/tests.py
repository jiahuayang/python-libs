# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:34
# @Author  : KaWa
# @File    : tests.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

from queue import Queue
from dqueue import Dqueue

if __name__ == "__main__":
    """test teh queue
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    """

    s = Dqueue()
    s.add_front(1)
    s.add_front(2)
    s.add_rear(3)
    s.add_rear(4)
    print(s.size())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_rear())
    print(s.pop_rear())