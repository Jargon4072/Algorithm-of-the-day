'''
Given a singly linked list, write a function to swap elements pairwise.

Input : 1->2->3->4->5->6->NULL
Output : 2->1->4->3->6->5->NULL

Input : 1->2->3->4->5->NULL
Output : 2->1->4->3->5->NULL



Input : 1->NULL
Output : 1->NULL

For example, if the linked list is 1->2->3->4->5 then the function should change it to 2->1->4->3->5, and if the linked list is then the function should change it to .

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=None
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next

        temp.next=new_node

        return
    def swap_pair(self):
        if self.head is None:
            return
        temp=self.head
        while temp.next is not None:
            nextp=temp.next
            z=temp.data
            temp.data=nextp.data
            nextp.data=z
            if(temp.next.next):
                temp=temp.next.next
            else:
                temp=temp.next
        return



    def print_list(self):
        if self.head is None:
            return
        temp=self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.next

        print("")

def main():
    ll=linkedlist()
    print("enter elements of Linked list: ")
    arr=[int(x) for x in input().strip().split()]
    for num in arr:
        ll.push(num)

    print("Created Linkedlist is: ")
    ll.print_list()

    print("performing pariwise swap! .......")
    ll.swap_pair()
    print("Modified List is: ")
    ll.print_list()

if __name__=="__main__":
    main()