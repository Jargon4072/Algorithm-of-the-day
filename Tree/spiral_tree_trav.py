from collections import deque
class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def tree_spiral_trav(root):
    if root ==None:
        return
    count=1
    dq=deque()
    dq.append(root)
    while True:
        dq2=deque()
        if count%2==0:
            while dq:
                node=dq.popleft()
                print(node.data,end=" ")
                if node.left:
                    dq2.append(node.left)

                if node.right:
                    dq2.append(node.right)
        else:
            while dq:
                node=dq.pop()
                print(node.data,end=" ")
                if node.left:
                    dq2.append(node.left)

                if node.right:
                    dq2.append(node.right)
        count+=1

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

    print("Spiral Traversal of tree: ")
    tree_spiral_trav(root)




