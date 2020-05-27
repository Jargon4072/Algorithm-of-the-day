class treenode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def ceil(self,root,val):
        if root==None:
            return -1

        elif root.data==val:
            return root.data

        # if root.data>val:
        #     root.left=self.ceil(root.left,val)

        elif root.data<val:
            return self.ceil(root.right,val)
        else:
            temp=self.ceil(root.left,val)
            if temp>=val:
                return temp
            else:
                return root.data
            # return temp if temp>=val else root.data



if __name__=="__main__":
    root = treenode(8)

    root.left = treenode(4)
    root.right = treenode(12)

    root.left.left = treenode(2)
    root.left.right = treenode(6)

    root.right.left = treenode(10)
    root.right.right = treenode(14)
    print(root.ceil(root,0))
