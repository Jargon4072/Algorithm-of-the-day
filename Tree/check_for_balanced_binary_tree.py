'''
Write a program to check if a tree is height balenced.

'''



class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def check_height_balanced(root,height):
    if root==None:
        return height

    lh=check_height_balanced(root.left,height+1)
    rh=check_height_balanced(root.right,height+1)
    return max(lh,rh)



def check_for_balanced_binary_tree(root):
    if root==None:
        return True

    lval=check_height_balanced(root.left,0)
    rval=check_height_balanced(root.right,0)
    if lval-rval<=1:
        return True
    else:
        return False



if __name__=="__main__":

    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)
    root.left.left.left = treenode(8)

    val=check_for_balanced_binary_tree(root)      #TODO: implement it in O(n)
    if val:
        print("Height Balenced! :)")
    else:
        print("Not Height balenced :(")



