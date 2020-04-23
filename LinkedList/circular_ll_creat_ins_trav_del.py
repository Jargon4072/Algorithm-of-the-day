# @Author: Dwivedi Chandan
# @Date:   2020-03-20T14:59:32+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-03-23T12:08:39+05:30

import gc

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circularlist:
    def __init__(self):
        self.head=None
    def push_front(self,data):
        if self.head==None:
            self.head=Node(data)
            self.head.next=self.head

        tmp1=Node(data)
        tmp2=self.head
        tmp1.next=self.head
        if self.head is not None:
            while(tmp2.next!=self.head):
                tmp2=tmp2.next
            tmp2.next=tmp1

        self.head=tmp1

    def printll(self):
        if self.head==None:
            return
        tmp=self.head
        while(tmp.next!=self.head):
            print(tmp.data, end=" ")
            tmp=tmp.next
        print("")

    def del_node(self,node):
        if(self.head==None):
            return
        tmp=self.head
        while(tmp.next!=self.head and tmp.next!=node):
            tmp=tmp.next

        if tmp.next==node:
            tmp.next=tmp.next.next

        gc.collect()

llist=circularlist()
print("Enter Numbers to insert at front: ")
arr=[int(x) for x in input().strip().split()]
for num in arr:
    llist.push_front(num)

print("List is: ")
llist.printll()

print("deleting third node from start.....")
dnode=llist.head.next.next
llist.del_node(dnode)
print("deleted third node")


print("List is: ")
llist.printll()


