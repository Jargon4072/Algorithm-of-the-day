class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def check_children_sum_property(root):
    if root==None:
        return True


    count=0
    if root.left:
        count+=root.left.data

    if root.right:
        count+=root.right.data

    if root.left==None and root.right==None:      #code to handle leaf node cases
        count=root.data
    if count==root.data:
        check_children_sum_property(root.left)
        check_children_sum_property(root.right)
    return False

if __name__=="__main__":
    root = treenode(5)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(1)
    root.left.right = treenode(1)
    root.right.left=treenode(2)
    root.right.right=treenode(1)
    val=check_children_sum_property(root)
    if val:
        print("Children Sum Property satisfied! :)")
    else:
        print("Children Sum property is NOT satisfied :(")