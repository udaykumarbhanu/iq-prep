'''Convert a Binary Tree into its Mirror Tree
Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with
left and right children of all non-leaf nodes interchanged.
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def inorder_print(self):
        if self.root is None:
            return

        self.inorder_print(self.root.left)
        print self.root
        self.inorder_print(self.root.right)

    def mirror(self):
        if self.root is None:
            return

        temp_node = self.root
        self.mirror(self.root.left)
        self.mirror(self.root.right)

        temp_node = self.root.left
        self.root.left = self.root.right
        self.root.right = temp_node

if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)
    fifth_node = Node(5)

    bt = BinaryTree()
    bt.root = first_node
    bt.root.left = second_node
    bt.root.right = third_node
    bt.root.left.left = fourth_node
    bt.root.right.right = fifth_node

    bt.inorder_print()
    
