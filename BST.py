class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, current, val):
        if self.root == None:
            self.root = Node(val)
        else:
            if val < current.val:
                if not current.left:
                    current.left = Node(val)
                else:
                    self.add(current.left, val)

            elif val > current.val:
                if not current.right:
                    current.right = Node(val)
                else:
                    self.add(current.right, val)



    def preorder(self, root):
        if root is None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
# -- TEST CASES --

# Creating BST instance
tree = BST()

# Adding nodes
values = [10, 5, 15, 3, 7, 13, 18]
for val in values:
    tree.add(tree.root, val)
# Expected BST structure:
#          10
#         /  \
#        5    15
#       / \   / \
#      3   7 13  18


# Testing preorder traversal
tree.preorder(tree.root)  # Expected output order: 10, 5, 3, 7, 15, 13, 18

# Testing preorder traversal
tree.preorder(tree.root)  # Expected output order: 10, 5, 3, 7, 15, 13, 18






