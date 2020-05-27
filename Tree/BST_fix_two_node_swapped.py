'''


'''

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def get_node_util(self,root,arr):
        if root==None:
            return
        self.get_node_util(root.left,arr)
        arr.append(root.data)
        self.get_node_util(root.right,arr)
    def fix_nodes(self,root,n1,n2):   # TODO: remove this function and modify get_node_util() to take prev and curr node and fix the bst.
        if root==None:
            return
        if root.data==n1:
            root.data=n2
        elif root.data==n2:
            root.data=n1
        self.fix_nodes(root.left,n1,n2)
        self.fix_nodes(root.right,n1,n2)
    def fix_bst(self,root):
        if root==None:
            return
        arr=[]
        self.get_node_util(root,arr)
        n1=-1
        n2=-1
        prev =arr[0]
        curr=0
        next=0
        n1=-1
        n2=-1
        for i in range(1,len(arr)):
            curr=arr[i]
            if curr<prev:
                if n1<0 and n2<0:
                    n1=prev
                elif n2<0 and n1>=0:
                    n2=curr
            prev=curr

        print("n1: "+str(n1))
        print("n2: "+str(n2))
        self.fix_nodes(root,n1,n2)
        return root

    def trav_tree(self,root):
        if root==None:
            return

        self.trav_tree(root.left)
        print(root.data, end=" ")
        self.trav_tree(root.right)

if __name__=="__main__":
    root = treenode(6);
    root.left        = treenode(10);
    root.right       = treenode(2);
    root.left.left  = treenode(1);
    root.left.right = treenode(3);
    root.right.right = treenode(12);
    root.right.left = treenode(7);
    print("Inorder Traversal before fixing:", end=" ")
    root.trav_tree(root)
    print("")
    print("Inorder Traversal after fixing:", end=" ")
    root.fix_bst(root)
    root.trav_tree(root)




