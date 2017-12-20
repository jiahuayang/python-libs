# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午10:29
# @Author  : KaWa
# @File    : tests.py
# @Project : dl-demo
# @Copyright(c) 2017 By KaWa All rights reserved.

from binary_tree import BinaryTree


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder_travel(tree.root)
    print(" ")
    tree.inorder_travel(tree.root)
    print(" ")
    tree.postorder_travel(tree.root)
    print(" ")
