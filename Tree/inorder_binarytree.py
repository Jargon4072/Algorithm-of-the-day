# @Author: Dwivedi Chandan
# @Date:   2020-04-13T23:58:40+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-05-17T22:15:03+05:30

'''
Write a code to print inorder traversal of a tree.
1. implement it recursively
2. implement it Iteratively
'''


class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def inorder_trav_rec(root):
    if root:
        inorder_trav_rec(root.left)
        print(root.data,end=" ")
        inorder_trav_rec(root.right)

def inorder_iterative(head):
    if head:
        root=head
        val=[]
        while True:
            if root:
                val.append(root)
                root=root.left

            elif val:
                root=val.pop()
                print(root.data,end=" ")
                root=root.right
            else:
                break
        print("")

if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)

    print("Inorder Traversal (Recursive): ")
    inorder_trav_rec(root)
    print("")
    print("Inorder Traversal (Iterative)")
    inorder_iterative(root)




