# @Author: Dwivedi Chandan
# @Date:   2020-04-21T00:29:56+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-05-17T22:37:04+05:30

#################################################################################------|
'''                                                                                    |
Problem Statement:                                                                     |
                                                                                       |
Given a binary tree, a target node in the binary tree, and an integer value k,         |
print all the nodes that are at distance k from the given target node.                 |
No parent pointers are available.                                                      |
                                                                                       |
'''#                                                                                   |
#################################################################################------|


class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def nodes_at_k_distance(root,k):
    if root==None or k<0:
        return
    if k==0:
        print(root.data)
        return

    nodes_at_k_distance(root.left,k-1)
    nodes_at_k_distance(root.right,k-1)

def nodes_at_k_distance_fmtarget(root,target,k):
    if root==None:
        return -1

    if root==target:
        nodes_at_k_distance(root,k)
        return 0
    dl=nodes_at_k_distance_fmtarget(root.left,target,k)
    if dl!=-1:
        if dl+1==k:
            print(root.data)

        else:
            nodes_at_k_distance(root.right,k-dl-2)
        return 1+dl

    dr=nodes_at_k_distance_fmtarget(root.right,target,k)
    if dr!=-1:
        if dr+1==k:
            print(root.data)
        else:
            nodes_at_k_distance(root.left,k-dr-2)
        return 1+dr

    return -1

if __name__=="__main__":
    root = treenode(20)
    root.left = treenode(8)
    root.right = treenode(22)
    root.left.left = treenode(4)
    root.left.right = treenode(12)
    root.left.right.left = treenode(10)
    root.left.right.right = treenode(14)
    target = root.left.right
    nodes_at_k_distance_fmtarget(root, target, 2)






