
def rotate(arr,k):
    res=arr[k:]
    for i in range(0,k):
        res.append(arr[i])
    return res

def main():
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        arr=list(map(int,input().split()))
        #print(arr)
        k=int(input())
        val=rotate(arr,k)
        for i in val:
            print(i,end=" ")
        print("")

if __name__=="__main__":
    main()