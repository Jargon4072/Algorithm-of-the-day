'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


'''



class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    #below method runs with O(N^2) time. To OPTIMIZE it we will have to modify height() function
    # def height(self,root):
    #     if root==None:
    #         return 0;
    #
    #     lh=self.height(root.left)
    #     rh=self.height(root.right)
    #     return max(lh,rh)+1
    #
    # def diameter(self,root):
    #     if root==None:
    #         return 0
    #
    #     ld=self.diameter(root.left)
    #     rd=self.diameter(root.right)
    #     lh=self.height(root.left)
    #     rh=self.height(root.right)
    #     return max(lh+rh+1,max(ld,rd))


    #below method runs with O(N) time.
    def heightopt(self,root, ans):
        if root==None:
            return 0

        lh=self.heightopt(root.left,ans)
        rh=self.heightopt(root.right,ans)
        ans[0]=max(ans[0],1+lh+rh)
        return 1+max(lh,rh)

    def diameteropt(self,root):
        if root==None:
            return 0

        ans=[-999999999999]
        height_tree=self.heightopt(root,ans)
        return ans[0]

if __name__=="__main__":
    root = treenode(1)
    root.left = treenode(2)
    root.right = treenode(3)
    root.left.left = treenode(4)
    root.left.right = treenode(11)
    root.right.left=treenode(6)
    root.right.right=treenode(7)

    dia=root.diameteropt(root)
    print("diameter of tree is: "+str(dia))
