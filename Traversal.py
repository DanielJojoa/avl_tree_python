#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def preorder(tree):
    __preorder(tree.root)


def __preorder(subtree):
    if subtree is not None :
        __visit_node(subtree)
        __preorder(subtree.left)
        __preorder(subtree.right)

def __visit_node(subtree, key_subtree=None, with_children=True):
      
        print("[" + str(subtree.key) + "]", end = " ")
        print(" " if key_subtree is None else "<-->" + str(key_subtree))
        if with_children:
            print(("O" if subtree.left is not None else "X") + ":" +
                ("O" if subtree.right is not None else "X") + "\n")
                
                
        return None        

