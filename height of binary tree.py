

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root==None:
        return -1
    ld=height(root.left)
    rd=height(root.right)
    if ld>rd:
        return ld+1
    else:
        return rd+1

