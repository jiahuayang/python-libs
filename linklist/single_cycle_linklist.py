# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午3:03
# @Author  : KaWa
# @File    : single_cycle_link_list.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

"""""""""""
A module to implement the single cycle link list
"""""""""""

# library
# standard library

# third-party library
from single_linklist import SingleLinkList

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(SingleLinkList):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node

    def length(self):
        """single cycly link list length"""
        if SingleLinkList.is_empty(self):
            return 0

        cur = self._head
        count = 1
        while cur.next != self._head:
            cur = cur.next
            count += 1

        return count

    def travel(self):
        """travel the whole single cycle link list and print it"""
        if SingleLinkList.is_empty(self):
            return

        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=" ")
            cur = cur.next
        # exit while and print the tail node elem
        print(cur.elem)

    def add(self, item):
        """add item at the head of the single cycle link list"""
        node = Node(item)
        if SingleLinkList.is_empty(self):
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # exit while, the cur pointer link to the tail node
            node.next = self._head
            self._head = node
            cur.next = node   # or cur.next = self._head

    def append(self, item):
        """add item at the tail of the single cycle link list"""
        node = Node(item)
        if SingleLinkList.is_empty(self):
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head      # or node.next = cur.next
            cur.next = node

    def insert(self, pos, item):
        """add the node at link's position, pos start with '0' """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # exit while loop, pre pointer link to (pos-1) node
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if SingleLinkList.is_empty(self):
            return
        cur = self._head
        pre = None

        while cur.next != self._head:
            if cur.elem == item:
                # find the item to remove
                # if the item is head node or not
                if cur == self._head:
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    # the item is at middle node
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

        # exit while loop, cur pointer to tail end
        if cur.elem == item:
            if cur == self._head:
                # one node
                self._head = Node
            else:
                pre.next = self._head    # or pre.next = cur.next

    def search(self, item):
        """search the node(item)"""
        if SingleLinkList.is_empty(self):
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # exit while loop, cur pointer link to the tail node
        if cur.elem == item:
            return True
        return False
