class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def tree_size(root):
    if root==None:
        return
    global size
    size=size+1
    tree_size(root.left)
    tree_size(root.right)

if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)
    root.right.left=treenode(6)
    root.right.right=treenode(7)

    size=0
    tree_size(root)
    print("size of tree is: "+str(size))
