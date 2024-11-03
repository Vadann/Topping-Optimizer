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

    # Test comment



