'''


'''

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def inorder_trav(self,root,arr):
        if root==None:
            return

        self.inorder_trav(root.left,arr)
        arr.append(root.data)
        self.inorder_trav(root.right,arr)

    def kth_smallest(self,root,k):    # TODO: this code take O(n) and O(h). make it O(h) by traversing in same func. and keeping rank
        if root==None:
            return

        arr=[]
        root.inorder_trav(root,arr)
        if k<=len(arr):
            return arr[k-1]
        else:
            return -1


if __name__=="__main__":
    root=treenode(20)
    root.left=treenode(8)
    root.right=treenode(22)
    root.left.left=treenode(4)
    root.left.right=treenode(12)
    root.left.right.left=treenode(10)
    root.left.right.right=treenode(14)

    k=5
    val=root.kth_smallest(root,k)
    print("k=%dth smallest value is %d"%(k,val))


