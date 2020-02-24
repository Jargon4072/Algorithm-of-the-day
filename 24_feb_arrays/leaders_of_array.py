def leaders(arr):
    res=[]
    max=arr[len(arr)-1]
    n=len(arr)-1
    for i in range(0,len(arr)):
        if(arr[n-i]>=max):
            #print(arr[n-i],end=" ")
            res.append(arr[n-i])
            max=arr[n-i]
    p=len(res)-1
    for i in range(len(res)):
        print(res[p-i],end=" ")
    print("")


if __name__=="__main__":
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        arr=list(map(int,input().split()))
        #print(arr)
        leaders(arr)