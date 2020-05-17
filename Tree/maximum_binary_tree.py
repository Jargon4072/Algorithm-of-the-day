'''

Given a binary tree. Return maximum element of it.

'''

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def maximum_binary_tree(root):
    if root==None:
        return
    global maximum
    if root.data>maximum:
        maximum=root.data
    maximum_binary_tree(root.left)
    maximum_binary_tree(root.right)


if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(11)
    root.right.left=treenode(6)
    root.right.right=treenode(7)

    maximum=0
    maximum_binary_tree(root)
    print("Maximum in Binary tree is:"+str(maximum))