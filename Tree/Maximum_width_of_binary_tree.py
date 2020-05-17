'''

Given a binary tree, write a function to get the maximum width of the given tree. Width of a tree is maximum of widths of all levels.
Let us consider the below example tree.

         1
        /  \
       2    3
     /  \     \
    4    5     8
              /  \
             6    7
For the above tree,
width of level 1 is 1,
width of level 2 is 2,
width of level 3 is 3
width of level 4 is 2.

So the maximum width of the tree is 3.

'''

from collections import deque
class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def max_width_tree(root):
    if root==None:
        return 0

    dq=deque()
    count=1
    dq.append(root)
    while True:
        dq2=deque()
        while dq:
            node=dq.popleft()
            if node.left:
                dq2.append(node.left)

            if node.right:
                dq2.append(node.right)

        count=max(count,len(dq2))
        dq=dq2
        if not dq:
            break
    return count

if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)
    root.right.right = treenode(8)
    root.right.right.left = treenode(6)
    root.right.right.right = treenode(7)

    print("Maximum Width of the binary tree is: "+str(max_width_tree(root)))

