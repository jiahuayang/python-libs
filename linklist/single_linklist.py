# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 下午8:06
# @Author  : KaWa
# @File    : single_linklist.py
# @Project : python-libs
# @Copyright(c) 2017 By KaWa All rights reserved.

"""""""""""
A module to implement the single link list
"""""""""""

# library
# standard library


# third-party library


class Node:
    """the "node" contains elem and next for the single link list
       "elem" is data, and "next" link to the next node"""
    def __init__(self, elem):
        self.elem = elem
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
        """travel the whole link and print the elem"""
        cur = self._head

        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

        print()

    def add(self, elem):
        """add the node at the link's head"""
        node = Node(elem)
        node.next = self._head
        self._head = node

    def append(self, elem):
        """add the node at the link's tail"""
        node = Node(elem)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, elem):
        """add the node at link's position, pos start with '0' """
        if pos <= 0:
            # add at the head
            self.add(elem)

        elif pos > (self.length()-1):
            # add at the tail
            self.append(elem)
            
        else:
            pre = self._head
            count = 0
            while count < (pos-1):
                pre = pre.next
                count += 1
            node = Node(elem)
            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        """remove the link's node(elem)"""
        cur = self._head
        pre = Node
        while cur != Node:
            if cur.elem == elem:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, elem):
        """search the elem at link, return true or false"""
        cur = self._head
        while cur != None:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next

        return False