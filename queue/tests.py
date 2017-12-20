# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:34
# @Author  : KaWa
# @File    : tests.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

from queue import Queue

if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())