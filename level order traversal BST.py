

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def depth(root):
    if root is None:
        return 0
    ld = depth(root.left)
    rd = depth(root.right)
    if ld>rd:
        return ld+1
    else:
        return rd+1

def printCurrentLevel(root, i):
    if root is None:
        return 0
    if i==1:
        print(root.info, end=" ")
    else:
        printCurrentLevel(root.left, i-1)
        printCurrentLevel(root.right, i-1)

def levelOrder(root):
    #Write your code here
    td = depth(root)
    for i in range(1,td+1):
        printCurrentLevel(root, i)


