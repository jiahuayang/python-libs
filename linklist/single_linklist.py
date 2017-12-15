# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 下午8:06
# @Author  : KaWa
# @File    : single_linklist.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

"""""""""""
A module to implement the single link list
"""""""""""

# library
# standard library


# third-party library


class Node:
    """the "node" contains item and next for the single link list
       "item" is data, and "next" link to the next node"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    def __init__(self):
        # _head link to the link's head pointer
        self._head = None

    def is_empty(self):
        """link is empty or not, return true or false"""
        # return self._head == None
        return not self._head

    def length(self):
        """return the link length"""
        cur = self._head
        count = 0

        while cur != None:
            count +=1
            cur = cur.next

        return count

    def travel(self):
        """travel the whole link and print the item"""
        cur = self._head

        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next

        print()

    def add(self, item):
        """add the node at the link's head"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """add the node at the link's tail"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """add the node at link's position, pos start with '0' """
        if pos <= 0:
            # add at the head
            self.add(item)

        elif pos > (self.length()-1):
            # add at the tail
            self.append(item)
            
        else:
            pre = self._head
            count = 0
            while count < (pos-1):
                pre = pre.next
                count += 1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """remove the link's node(item)"""
        cur = self._head
        pre = Node
        while cur != Node:
            if cur.item == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """search the item at link, return true or false"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next

        return False