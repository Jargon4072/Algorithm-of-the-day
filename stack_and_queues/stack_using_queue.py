'''
We are given a Queue data structure that supports standard operations like enqueue() and dequeue(). We need to implement a Stack data structure using only instances of Queue and queue operations allowed on the instances.

'''



from queue import Queue

class stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.curr_size=0

    def push(self, data):
        self.curr_size+=1
        if self.q1.empty() and self.q1.empty():
            self.q1.put(data)
        elif self.q1.empty() and not self.q2.empty():
            self.q2.put(data)
        elif self.q2.empty() and not self.q1.empty():
            self.q1.put(data)

    def pop(self):
        if self.q1.empty() and self.q2.empty():
            print("Stack Underflow. Nothing to pop!")
        elif self.q1.empty() and not self.q2.empty():
            val=0
            while not self.q2.empty():
                val=self.q2.get()
                if self.q2.empty():
                    self.curr_size=self.curr_size-1
                    return val
                self.q1.put(val)

        elif self.q2.empty() and not self.q1.empty():
            val=0
            while not self.q1.empty():
                val=self.q1.get()
                if self.q1.empty():
                    self.curr_size=self.curr_size-1
                    return val
                self.q2.put(val)

    def top(self):
        if self.q1.empty() and self.q2.empty():
            return -1

        elif self.q1.empty() and not self.q2.empty():
            return self.q2.queue[self.curr_size-1]
        elif self.q2.empty() and not self.q1.empty():
            return self.q1.queue[self.curr_size-1]


if __name__=="__main__":
    st=stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(9)
    st.push(11)
    print("Current size of stack: "+str(st.curr_size))
    print("top of stack: "+str(st.top()))
    print("Performing pop operation. ")
    val=st.pop()
    print("poped value is: "+str(val))
    print("Current size of stack: "+str(st.curr_size))
    print("Performing pop operation. ")
    val=st.pop()
    print("poped value is: "+str(val))
    print("Current size of stack: "+str(st.curr_size))



