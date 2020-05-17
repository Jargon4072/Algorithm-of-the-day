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

    def delete(self,root,value):
        '''Three cases to consider
        CASE 1: Node to be deleted is leaf: Simply remove from the tree.
        CASE 2: Node to be deleted has only one child: Copy the child to the node and delete the child
        CASE 3: Node to be deleted has two children: Find inorder successor/predecessor  of the node. Copy contents of the inorder successor/predecessor  to the node and delete the inorder successor/predecessor.'''

    