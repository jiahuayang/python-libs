# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午10:11
# @Author  : KaWa
# @File    : binary_tree.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

# library
# standard library

# third-party library


class Node:
    """binary tree node"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self):
        # initialize the root node
        self.root = None

    def add(self, item):
        # add node by breadth
        node = Node(item)
        if self.root is None:
            # binary tree has only root node
            self.root = node
            return

        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """breadth travel the binary tree"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")

            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder_travel(self, node):
        """preorder travel the binary tree"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder_travel(node.lchild)
        self.preorder_travel(node.rchild)

    def inorder_travel(self, node):
        """inorder travel the binary tree"""
        if node is None:
            return
        self.inorder_travel(node.lchild)
        print(node.elem, end=" ")
        self.inorder_travel(node.rchild)

    def postorder_travel(self, node):
        """postorder travel the binary tree"""
        if node is None:
            return
        self.postorder_travel(node.lchild)
        self.postorder_travel(node.rchild)
        print(node.elem, end=" ")