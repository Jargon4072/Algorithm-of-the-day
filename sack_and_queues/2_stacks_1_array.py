class twostack:
    def __init__(self,n):
        self.size=n
        self.p1=-1
        self.p2=self.size
        self.arr=[None]*n

    def push1(self,data):
        self.p1=self.p1+1
        if self.p1==self.p2:
            print("Stack Overflow!")
            return
        self.arr[self.p1]=data
        return
    def push2(self,data):
        self.p2=self.p2-1
        if self.p1==self.p2:
            print("Stack Overflow!")
            return
        self.arr[self.p2]=data
        return

    def pop1(self):
        if self.p1<0:
            print("Stack 1 is empty!")
            return
        value=self.arr[self.p1]
        self.p1=self.p1-1
        return value


    def pop2(self):
        if self.p2==self.size:
            print("Stack2 is empty!")
            return
        value=self.arr[self.p2]
        self.p2=self.p2+1
        return value


def main():
    print("Enter Size of array: ")
    size=int(input())
    ts=twostack(size)

    while True:
        print("\n\n")
        print("Select operations:")
        print("1. push into stack1")
        print("2. push into stack2")
        print("3. pop from stack1")
        print("4. pop from stack2")
        print("5. Exit")
        print("Enter your choice!")
        inval=int(input())
        if inval==1:
            print("Enter number to push")
            num=int(input())
            ts.push1(num)

        if inval==2:
            print("Enter number to push")
            num=int(input())
            ts.push2(num)

        if inval==3:
            num=ts.pop1()
            print("value poped: "+str(num))

        if inval==4:
            num=ts.pop2()
            print("value poped: "+str(num))

        if inval==5:
            return

if __name__ == '__main__':
    main()
