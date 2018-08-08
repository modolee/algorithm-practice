class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def findAncestor(root, val):
    curr = root
    result = []

    while curr.info != val:
        result.append(curr.info)
        if val < curr.info:
            curr = curr.left
        else:
            curr = curr.right

    result.append(curr.info)

    return result


def lca(root, v1, v2):
    # Enter your code here
    v1_ancestor = findAncestor(root, v1)
    v2_ancestor = findAncestor(root, v2)
    if len(v1_ancestor) > len(v2_ancestor):
        longer = v1_ancestor
        shorter = v2_ancestor
    else:
        longer = v2_ancestor
        shorter = v1_ancestor

    while not longer[-1] in shorter:
        longer.pop()

    return Node(longer[-1])


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
