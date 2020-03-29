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
    def reverse(self,node):
        if node.next is None:
            self.head=node
            return
        self.reverse(node.next)
        temp=node.next
        temp.next=node
        node.next=None

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

    print("Reversing the list recersively! .......")
    ll.reverse(ll.head)
    print("Reversed List is: ")
    ll.print_list()

if __name__=="__main__":
    main()