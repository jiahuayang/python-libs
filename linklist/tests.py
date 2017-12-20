# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 下午8:54
# @Author  : KaWa
# @File    : tests.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.


# library
# stand library

# third-party library


from single_linklist import SingleLinkList
from single_cycle_linklist import SingleCycleLinkList
from double_linklist import DoubleLinkList


if __name__ == '__main__':
    """
    # test single link list
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
    """

    """test single cycle link list
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
    """

    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()

    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
