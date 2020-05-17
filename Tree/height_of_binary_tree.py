'''

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''



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
