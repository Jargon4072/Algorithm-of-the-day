'''


'''

class treenode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def check_bst_util(self,root,min,max):
        if root==None:
            return True

        if root.data<min or root.data>max:
            return False

        return self.check_bst_util(root.left,min,root.data-1) and self.check_bst_util(root.right,root.data-1,max)


    def check_bst(self,root):
        return self.check_bst_util(root,0,999999999)


if __name__=="__main__":
    root=treenode(20)
    root.left=treenode(8)
    root.right=treenode(22)
    root.left.left=treenode(4)
    root.left.right=treenode(12)
    root.left.right.left=treenode(10)
    root.left.right.right=treenode(14)

    res=root.check_bst(root)
    if res:
        print("Given Tree is BST")
    else:
        print("Given Tree is not BST")