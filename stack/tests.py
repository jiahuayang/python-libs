# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午5:09
# @Author  : KaWa
# @File    : tests.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

from stack import Stack

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.peek())
    s.push(3)
    s.push(4)
    print(s.size())

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())