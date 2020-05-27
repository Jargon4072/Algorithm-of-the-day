'''


'''


class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def pair_sum_util(self,root,ele):
        if root==None:
            return
        self.pair_sum_util(root.left,ele)
        ele.append(root.data)
        self.pair_sum_util(root.right,ele)
    def findTarget(self, root, k: int) -> bool:       #optimized method!
        ele=[]
        self.pair_sum_util(root,ele)
        if not ele:
            print("No such pair exist for sum value %d."%k)
            # return False
        h_map=[0]*999999
        if len(ele)>1:
            for item in ele:
                h_map[item]+=1
                if h_map[k-item]>0 and k-item!=item:
                    print("Pair Found! the required pairs are: %d,%d"%(k-item,item))
                    return
                    # return True

        # return False
        print("No such pair exist for sum value %d."%k)

    def insert(self,root,value):
        if root==None:
            root=treenode(value)
            return root
        if value<root.data:
            root.left=self.insert(root.left,value)
        if value>root.data:
            root.right=self.insert(root.right,value)

        return root


if __name__=="__main__":
    print("Inserting 15, 10, 20, 8, 12, 16, 25, 10 in the BST respectively.")
    root=treenode(15)
    root = root.insert(root,10)
    root = root.insert(root,20)
    root = root.insert(root,8)
    root = root.insert(root,12)
    root = root.insert(root,16)
    root = root.insert(root,25)
    root = root.insert(root,10)

    print("Enter value of Sum: ")
    sum=int(input())
    root.findTarget(root,sum)


