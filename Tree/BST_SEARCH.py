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

    def search(self,root,value):
        if root==None:
            return False
        result=False
        if root.data==value:
            result=True
            return result
        if root.data>value:
            result=self.search(root.left,value)

        elif root.data<value:
            result=self.search(root.right,value)

        return result

if __name__=="__main__":
    print("Enter elements to create tree: ")
    array=[int(x) for x in input().strip().split()]
    root=treenode(array[0])
    for i in range(1,len(array)):
        root.insert(root,array[i])

    print("Enter element to search: ")
    val=int(input())
    res=root.search(root,val)
    out="Entered key is present in tree" if res else "Entered key is not present in the tree"
    print(out)



