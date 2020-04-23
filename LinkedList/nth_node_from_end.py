class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
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

    def nth_node_fmend(self,N):
        if self.head is None:
            return
        temp=self.head
        count=0
        while temp:
            count=count+1
            temp=temp.next

        temp1=self.head
        for i in range(1,count-N+1):
            temp1=temp1.next
        return temp1

    def print_linkedlist(self):
        if self.head is None:
            return
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

        print("")


def main():
    print("Enter Linked list elements: ")
    ll=linkedlist()
    arr=[int(x) for x in input().strip().split()]
    for num in arr:
        ll.push(num)
    print("Enter value of N: ")
    N=int(input())
    print("Entered Linked List is: ")
    ll.print_linkedlist()
    res=ll.nth_node_fmend(N)
    print("{} node from end is: {}".format(N,res.data))

if __name__=="__main__":
    main()
