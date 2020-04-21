# @Author: Dwivedi Chandan
# @Date:   2020-04-21T00:29:56+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-04-21T09:54:04+05:30

#################################################################################------|
# Problem Statement:                                                                   |
#                                                                                      |
# Given a binary tree, a target node in the binary tree, and an integer value k,       |
# print all the nodes that are at distance k from the given target node.               |
# No parent pointers are available.                                                    |
#                                                                                      |
#################################################################################------|


class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def nodes_at_k_distance(node,k):
    if node==None:
        return


