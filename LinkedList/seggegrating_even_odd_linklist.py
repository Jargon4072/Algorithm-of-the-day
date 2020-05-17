'''
Given a Linked List of integers, write a function to modify the linked list such that all even numbers appear before all the odd numbers in the modified linked list. Also, keep the order of even and odd numbers same.

Examples:

Input: 17->15->8->12->10->5->4->1->7->6->NULL
Output: 8->12->10->4->6->17->15->5->1->7->NULL

Input: 8->12->10->5->4->1->6->NULL
Output: 8->12->10->4->6->5->1->NULL

// If all numbers are even then do not change the list
Input: 8->12->10->NULL
Output: 8->12->10->NULL

// If all numbers are odd then do not change the list
Input: 1->3->5->7->NULL
Output: 1->3->5->7->NULL
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
    def seggegrate(self):
        if self.head is None:
            return
        temp=self.head
        llodd=linkedlist()
        lleven=linkedlist()
        while temp is not None:
            if temp.data%2==0:
                lleven.push(temp.data)
            else:
                llodd.push(temp.data)

            temp=temp.next

        temp1=lleven.head
        while temp1.next is not None:
            temp1=temp1.next
        temp1.next=llodd.head
        return lleven.head



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

    print("seggegrating even odd! .......")
    ll.head=ll.seggegrate()
    print("seggegrated List is: ")
    ll.print_list()

if __name__=="__main__":
    main()