class kstack:
    def __init__(self,k,n):
        self.size=n
        self.k=k
        self.nextIndex=[i for i in range(1,self.size)]
        self.nextIndex.append(-1)
        self.s=[0]*self.size
        self.free=0
        self.top=[-1]*self.k

    def isempty(self,sn):
        if self.top[sn]==-1:
            return True
        return False

    def isfull(self):
        if self.free==-1:
            return True
        return False

    def push(self,sn,value):
        if self.isfull():
            print("Stack Overflow occured!")
            return
        self.s[self.free]=value
        tmp=self.free
        self.free=self.nextIndex[self.free]
        self.nextIndex[tmp]=self.top[sn]
        self.top[sn]=tmp

    def pop(self,sn):
        if self.isempty(sn):
            print("Can't pop. Stack is empty!")
            return None

        idx=self.top[sn]
        res=self.s[idx]
        self.top[sn]=self.nextIndex[idx]
        self.nextIndex[idx]=self.free
        self.free=idx
        return res

    def printstack(self,sn):
        idx=self.top[sn]
        while idx!=-1:
            print(self.s[idx])
            idx=self.nextIndex[idx]


def main():
    st=kstack(3,6)
    print("operation: push 5 into stack 0")
    st.push(0,5)
    print("operation: push 6 into stack 0")
    st.push(0,6)
    print("operation: push 7 into stack 1")
    st.push(1,7)
    print("Printing stack 0: ")
    st.printstack(0)
    print("Printing stack 1:")
    st.printstack(1)
    print("operation: pop from stack 0")
    print("popped value: "+str(st.pop(0)))
    print("Stack 0 is now: ")
    st.printstack(0)
    print("operation: push 8 into stack 2")
    st.push(2,8)
    print("Stack 2 is: ")
    st.printstack(2)


if __name__=="__main__":
    main()