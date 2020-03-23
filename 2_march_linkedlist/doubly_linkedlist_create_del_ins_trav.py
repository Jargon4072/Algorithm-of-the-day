# @Author: Dwivedi Chandan
# @Date:   2020-03-15T17:43:46+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-03-23T11:50:12+05:30

import gc

class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data


class Doublyll:
    def __init__(self):
        self.head=None

    def push_front(self, new_data):           #function to push a node at front of doubly linkedlist
        new_node=Node(new_data)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node

        self.head=new_node
    def push_back(self,new_data):
        new_node=Node(new_data)
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

    def push_after(self,prev_node, new_data):
        new_node=Node(new_data)
        new_node.next=prev_node.next
        new_node.prev=prev_node
        prev_node.next=new_node
        if new_node.next is not None:
            new_node.next.prev=new_node

    def push_before(self,curr_node,new_data):
        new_node=Node(new_data)
        new_node.next=curr_node
        new_node.prev=curr_node.prev
        curr_node.prev=new_node


    def del_node(self,node):
        if self.head is None or node is None:
            return
        if(self.head==node):
            self.head=node.next

        if(node.next is not None):
            node.next.prev=node.prev

        if(node.prev is not None):
            node.prev.next=node.next

        gc.collect()



    def printll(self):
        if self.head is not None:
            tmp=self.head
            while tmp is not None:
                print(tmp.data, end=" ")
                tmp=tmp.next

            print("")


llist=Doublyll()
print("enter numbers: ")
# scan numbers to form linkedlist
arr=[int(x) for x in input().strip().split()]
for num in arr:
    llist.push_back(num)

print("List is: ")
llist.printll()

print("Enter number to push at front in linked list:")
x=int(input())

llist.push_front(x)

print("List is: ")
llist.printll()

print("deleting third node from start.....")
dnode=llist.head.next.next
llist.del_node(dnode)
print("deleted third node")


print("List is: ")
llist.printll()









