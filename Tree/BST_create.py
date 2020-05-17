# @Author: Dwivedi Chandan
# @Date:   2020-05-14T14:30:24+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-05-17T19:16:03+05:30

'''
Write a code to insert in a BST. Goal it to take input from user and create BST from it by inserting elements in BST

'''

class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,root,value):
        if root==None:
            root=treenode(value)
            return root

        if root.data>value:
            root.left=self.insert(root.left,value)

        elif root.data<value:
            root.right=self.insert(root.right,value)

        return root

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

if __name__=="__main__":
    print("Enter elements to create tree: ")
    array=[int(x) for x in input().strip().split()]
    #print(array)
    print("Creatting tree from above entered elements.......")
    #array=array.sort()

    root=treenode(array[0])
    for i in range(1,len(array)):
        val=array[i]
        root.insert(root,val)

    print("Inorder traversal of created tree is: ")
    root.inorder(root)
    print("")







