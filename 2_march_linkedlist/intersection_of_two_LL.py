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
    def intersection(self,ll):
        if not self.head or not ll.head:
            return
        list=[]
        temp=ll.head
        while temp is not None:
            list.append(temp.data)
            temp=temp.next
        temp2=self.head
        while temp2 is not None:
            if temp2.data in list:
                return temp2
            temp2=temp2.next
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
    ll1=linkedlist()
    ll2=linkedlist()
    print("enter elements of  first Linked list: ")
    arr1=[int(x) for x in input().strip().split()]
    for num in arr1:
        ll1.push(num)
    print("enter elements of  first Linked list: ")
    arr2=[int(x) for x in input().strip().split()]
    for num in arr2:
        ll2.push(num)
    print("Created first Linkedlist is: ")
    ll1.print_list()
    print("Created second Linkedlist is: ")
    ll2.print_list()

    print("intersectio of two list is: ")
    node=ll1.intersection(ll2)
    if node is not None:
        print(node.data)
    else:
        print("No intersectio found!")

if __name__=="__main__":
    main()