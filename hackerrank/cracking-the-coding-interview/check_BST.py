""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    left = root.left
    right = root.right
    checkLeft = False
    checkRight = False
    leftChildren = []
    rightChildren = []

    if left == None:
        checkLeft = True
    elif left.data >= root.data:
        return False
    else:
        leftChildren = childList(left)
        for child in leftChildren:
            if child >= root.data:
                return False
        checkLeft = checkBST(left)

    if right == None:
        checkRight = True
    elif right.data <= root.data:
        return False
    else:
        rightChildren = childList(right)
        for child in rightChildren:
            if child <= root.data:
                return False
        checkRight = checkBST(right)

    childrenList = []
    childrenList.append(root.data)
    if leftChildren:
        childrenList += leftChildren
    if rightChildren:
        childrenList += rightChildren

    childrenSet = set(childrenList)

    if len(childrenSet) == len(childrenList):
        return checkLeft and checkRight
    else:
        return False


def childList(root):
    left = root.left
    right = root.right
    children = []

    if left != None:
        children.append(left.data)
        leftChildren = childList(left)
        if leftChildren:
            children += leftChildren

    if right != None:
        children.append(right.data)
        rightChildren = childList(right)
        if rightChildren:
            children += rightChildren

    return children