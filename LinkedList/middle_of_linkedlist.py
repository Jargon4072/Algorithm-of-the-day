'''
PROBLEM STATEMENT:

Write a programe to find middle element of a linked list
'''



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def find_middle(self):
        if self.head==None:
            return
        if self.head.next.next is None:
            return self.head.next
        fast=self.head
        slow=self.head
        while fast and fast.next and slow and slow.next:
            slow=slow.next
            fast=fast.next.next

        if slow:
            return slow
        return

    def push(self,data):
        new_node=Node(data)
        new_node.next=None
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        return



    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next

        print("")

def main():
    ll=linkedlist()
    arr=[int(x) for x in input().strip().split()]

    for num in arr:
        ll.push(num)

    print("Created linkedlist is: ")
    ll.print_list()

    print("middle of linked list is: ",end=" ")
    res=ll.find_middle()
    print(res.data)

if __name__=="__main__":
    main()



