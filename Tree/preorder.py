class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preorder_rec(node):
    if node==None:
        return
    print(node.data,end=" ")
    preorder_rec(node.left)
    preorder_rec(node.right)

def preorder_ierative(root):
    if root == None:
        return
    node=root
    stack=[]
    while True:
        print(node.data,end=" ")
        if node.left:
            stack.append(node)
            node=node.left
        elif stack:
            node=stack.pop()
            node=node.right
        else:
            break
    print("")

if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)

    print("Preorder Traversal (Recursive): ")
    preorder_rec(root)
    print("")
    print("Preorder Traversal (Iterative)")
    preorder_ierative(root)


