class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class doublyll:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def binary_tree2Doubly_ll(root):
    if root==None:
        return
