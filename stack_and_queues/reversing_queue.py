'''
Give an algorithm for reversing a queue Q. Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue.
dequeue() : Remove an item from front of queue.
empty() : Checks if a queue is empty or not.
Examples:

Input : Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Output :Q = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

Input :[1, 2, 3, 4, 5]
Output :[5, 4, 3, 2, 1]

'''

from queue import Queue

def print_queue(iq):
    size=iq.qsize()
    for i in range(size):
        print(iq.queue[i],end=" ")
    print("")

def reverse_queue(iq):
    st=[]
    while not iq.empty():
        val=iq.get()
        st.append(val)
    for i in range(len(st)):
        iq.put(st[len(st)-i-1])
    return iq

if __name__=="__main__":
    q=Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    q.put(6)
    q.put(7)

    print("Enttered Queue is: ")
    print_queue(q)

    print("Reversing the Queue.........")
    print("Updated Queue is:")
    q=reverse_queue(q)
    print_queue(q)