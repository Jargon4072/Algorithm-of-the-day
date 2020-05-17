'''

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


'''


class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    """Note: Below implementation is for LCA using seprate travesal fuction. This can further optimized to find LCA in single travesal"""

    # def trav_tree(self,root,n,path):
    #     if root==None:
    #         return True
    #
    #     path.append(root.data)
    #     if root.data==n:
    #         # path.append(n)
    #         return True
    #
    #     if (root.left!= None and self.trav_tree(root.left,n,path)) or (root.right!= None and self.trav_tree(root.right,n,path)):
    #         return True
    #
    #     path.pop()
    #     return False
    #
    # def LCA_easy(self,root,n1,n2):
    #     p1=[]
    #     p2=[]
    #     if self.trav_tree(root,n1,p1) and self.trav_tree(root,n2,p2):
    #         prev=0
    #         for (x1,x2) in zip(p1,p2):
    #             if x1!=x2:
    #                 return prev
    #             prev=x1
    #     return -1

    """Note: Below code is optimised veriosn of above one. However this fails if one of given node is not present in tree. """
    # def LCA(self,root,n1,n2):
    #     if root==None:
    #         return None
    #
    #     if root.data==n1 or root.data==n2:
    #         return root
    #
    #     llca=self.LCA(root.left,n1,n2)
    #     rlca=self.LCA(root.right,n1,n2)
    #
    #     if llca and rlca:
    #         return root
    #
    #
    #     return llca if llca is not None else rlca

    '''
    Final solution!
    '''

    def findintree(self,root,k):
        if root==None:
            return False
        if root.data==k or self.findintree(root.left,k) or self.findintree(root.right,k):
            return True

        return False

    def LCAutil(self,root,n1,n2,v):
        if root==None:
            return None

        if root.data==n1 or root.data==n2:
            if root.data==n1:
                v[0]=True
            if root.data==n2:
                v[1]=True
            return root

        llca=self.LCAutil(root.left,n1,n2,v)
        rlca=self.LCAutil(root.right,n1,n2,v)

        if llca and rlca:
            return root

        return llca if llca is not None else rlca

    def LCA(self,root,n1,n2):
        if root==None:
            return None
        v=[False,False]

        lca=self.LCAutil(root,n1,n2,v)

        if v[0] and v[1] or (v[0] and self.findintree(root,n2)) and (v[1] and self.findintree(root,n1)):
            return lca

        return None


if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(5)
    root.right.left = treenode(6)
    root.right.right = treenode(7)

    val=root.LCA(root,4,5)
    print("LCA OF 4 & 5 is: "+str(val.data))
