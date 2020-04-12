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