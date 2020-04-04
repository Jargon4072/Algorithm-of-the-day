import gc
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=None
        self.hmap={}
        self.tail=None

    def get(self, key: int) -> int:
        if self.head is None:
            return -1
        if not key in self.hmap.keys():
            return -1
        node=self.hmap[key]
        if node is None:
            return -1
        if node ==self.head:
            return node.data
        new_node=Node(node.data)
        new_node.next=self.head
        if node == self.tail:
            if self.tail.prev is not None:
                self.tail=self.tail.prev
            else:
                self.tail=new_node
        if node.prev:
            node.prev.next=node.next
            node.next.prev=node.prev
        self.head=new_node
        gc.collect()
        self.hmap[key]=self.head
        return self.head.data
        

    def put(self, key: int, value: int) -> None:
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.hmap[key]=self.head
            return
        if len(self.hmap)<self.capacity:
            if not key in self.hmap.keys():
                self.hmap[key]=new_node
                new_node.next=self.head
                self.head=new_node
                return
            elif key in self.hmap.keys():
                res=self.get(key)
                return
        else:
            dnode=self.tail
            if self.tail and self.tail.prev:
                self.tail=self.tail.prev
            else:
                self.tail=new_node
            if dnode and dnode.prev:
                dnode.prev.next=dnode.next
                dnode.next.prev=dnode.prev
            new_node.next=self.head
            self.head=new_node
            return
            
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
