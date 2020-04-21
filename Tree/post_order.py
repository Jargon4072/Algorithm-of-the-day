class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def postorder_rec(root):
    if root==None:
        return

    postorder_rec(root.left)
    postorder_rec(root.right)
    print(root.data,end=" ")

def postorder_iterative(root):
    if root==None:
        return
    node=root
    stack=[]
    while True:
        while node!=None:
            stack.append(node)
            stack.append(node)
            node=node.left

        if not stack:
            break
        node =stack.pop()

        if (stack and stack[-1]==node):
            node=node.right

        else:
            print(node.data,end=" ")
            node=None
    print("")



if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)

    print("Postorder Traversal (Recursive): ")
    postorder_rec(root)
    print("")
    print("Postorder Traversal (Iterative)")
    postorder_iterative(root)