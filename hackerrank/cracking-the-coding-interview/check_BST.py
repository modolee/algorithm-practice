""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def recursiveBST(root, min, max):
    if root == None:
        return True
    if root.data <= min or root.data >= max:
        return False
    else:
        return recursiveBST(root.left, min, root.data) and recursiveBST(root.right, root.data, max)


def checkBST(root):
    return recursiveBST(root, -1, 10001)