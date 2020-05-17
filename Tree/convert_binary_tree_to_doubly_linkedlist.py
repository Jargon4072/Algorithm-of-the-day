'''

Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

ex:
			  1
		   /     \
		  2       3
		 / \     / \
		4   5   6   7

           to
        4 ⇆ 2 ⇆ 5 ⇆1 ⇆ 6 ⇆ 3 ⇆ 7 
'''


class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class DlNode:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data


class doublyll:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=DlNode(data)
        new_node.next=None
        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return

        tmp=self.head
        while tmp.next is not None:
            tmp=tmp.next

        tmp.next=new_node
        new_node.prev=tmp
        return
    def printll(self):
        if self.head is not None:
            tmp=self.head
            while tmp is not None:
                print(tmp.data, end=" ")
                tmp=tmp.next

            print("")

def inorder(root,list):
    if root==None:
        return
    inorder(root.left,list)
    list.append(root.data)
    inorder(root.right,list)

def binary_tree2Doubly_ll(root):
    if root==None:
        return
    val=[]
    inorder(root,val)
    dll=doublyll()
    for item in val:
        dll.insert(item)

    return dll


if __name__=="__main__":
    root = treenode(5)
    root.left = treenode(3)
    root.right = treenode(6)
    root.left.left = treenode(1)
    root.left.right = treenode(4)
    root.right.right = treenode(8)
    root.left.left.left = treenode(0)
    root.left.left.right = treenode(2)
    root.right.right.left = treenode(7)
    root.right.right.right = treenode(9)

    dll=doublyll()

    dll=binary_tree2Doubly_ll(root)
    print("printing linkedlist elements: ")

    dll.printll()





