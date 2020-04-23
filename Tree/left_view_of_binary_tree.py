from collections import deque
class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def print_left_view_tree(root):
    if root==None:
        return

    dq=deque()
    dq.append(root)
    print(root.data)
    while True:
        dq2=deque()
        while dq:
            node=dq.popleft()
            if node.left:
                dq2.append(node.left)

            if node.right:
                dq2.append(node.right)

        dq=dq2
        if dq:
            print(dq[0].data)
        if not dq2:
            break



if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)
    root.right.left=treenode(6)
    root.right.right=treenode(7)

    print("Left view of tree: ")
    print_left_view_tree(root)





