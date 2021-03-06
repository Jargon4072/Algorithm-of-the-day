'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7


return its level order traversal as:
  3
  9 20
  15 7

'''


from collections import deque

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelorder_trav(root):
    if root ==None:
        return
    dq=deque()
    dq.append(root)
    while True:
        dq2=deque()

        while dq:
            node=dq.popleft()
            print(node.data,end=" ")
            if node.left:
                dq2.append(node.left)

            if node.right:
                dq2.append(node.right)

        print("")

        dq=dq2
        if not dq2:
            break
    print("")


if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)
    root.right.left=treenode(6)
    root.right.right=treenode(7)

    print("Levelorder Traversal of tree: ")
    levelorder_trav(root)

