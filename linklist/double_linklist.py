# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午4:32
# @Author  : KaWa
# @File    : double_linklist.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

"""""""""""
A module to implement the double link list
"""""""""""

# library
# standard library

# third-party library
from single_linklist import SingleLinkList

class Node:
    """node for double link list"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(SingleLinkList):
    def __init__(self, node=None):
        self._head = node

    def add(self, item):
        """add node at the head of the double link list"""
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node

    def append(self, item):
        """add node at the tail of the double link list"""
        node = Node(item)
        if SingleLinkList.is_empty(self):
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """add the node at link's position, pos start with '0' """
        if pos <= 0:
            self.add(item)
        elif pos > (SingleLinkList.length(self)-1):
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """remove the node(item) at the double link list"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                # if the node is head node or not
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        # the double link list only one node
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
