'''Lowest Common Ancestor in a Binary Search Tree.
Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest Common Ancestor (LCA). You may assume that both the values exist in the tree.
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = self.left = None
