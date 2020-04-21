class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height_tree(root,height):
    if root==None:
        return height
    lheight=height_tree(root.left,height+1)
    rheight=height_tree(root.right,height+1)
    return max(lheight,rheight)



if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(11)
    root.right.left=treenode(6)
    root.right.right=treenode(7)

    height=height_tree(root,0)
    print("Height of tree is: "+str(height))
