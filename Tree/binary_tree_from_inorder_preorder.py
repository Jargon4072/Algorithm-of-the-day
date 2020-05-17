'''
Construct Tree from given Inorder and Preorder traversals
Let us consider the below traversals:

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F

Output:
Inorder traversal of the constructed tree is
D B E A F C

'''

class treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def print_inorder_tree(self, root):
        if root == None:
            return
        self.print_inorder_tree(root.left)
        print(root.data,end=" ")
        self.print_inorder_tree(root.right)

def construct_tree(inorder, preorder, istart, iend):
    if istart>iend:
        return None
    root=treenode(preorder[construct_tree.var])
    construct_tree.var=construct_tree.var+1
    if istart==iend:
        return root

    idx=search(inorder,istart,iend,root.data)
    root.left=construct_tree(inorder,preorder,istart,idx-1)
    root.right=construct_tree(inorder,preorder,idx+1,iend)
    return root
def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

if __name__ == "__main__":
    print("Enter Inorder Traversal sequence: ")
    inorder = [int(x) for x in input().strip().split()]
    print("Enter Preorder Traversal Sequence: ")
    preorder = [int(x) for x in input().strip().split()]
    construct_tree.var=0    #TODO: Explore more about this naming convention of variable

    root=construct_tree(inorder, preorder,0,len(inorder)-1)
    root.print_inorder_tree(root)
    print("")
