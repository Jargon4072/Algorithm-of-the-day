'''
PROBLEM STATEMENT

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''



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
