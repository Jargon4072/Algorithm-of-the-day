import gc
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

    def del_withouttouchinghead(self,node):
        if node is None:
            return
        if node.next is not None:
            node.data=node.next.data
            if node.next.next is not None:
                node.next=node.next.next

            else:
                node.next=None
        else:
            node=None

            gc.collect()

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

    print("Enter Linked list elements: ")
    arr=[int(x) for x in input().strip().split()]

    for num in arr:
        ll.push(num)

    print("The created list is: ")
    ll.print_list()

    print("Deleteing third node from start, without accessing head ......... ")
    node=ll.head.next.next
    ll.del_withouttouchinghead(node)
    print("Linked list after deletion: ")
    ll.print_list()

if __name__=="__main__":
    main()
