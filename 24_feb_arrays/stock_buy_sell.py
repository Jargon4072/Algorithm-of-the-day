
def stock_buy_sell(arr):
    flag=0
    if(len(arr)<=0):
        return
    min_v=[]
    max_v=[]
    n=len(arr)
    for i in range(0,len(arr)):
        if((i!=0 and i!=n-1 and arr[i]<arr[i-1] and arr[i]<arr[i+1]) or (i==0 and arr[i]<arr[i+1])):
            min_v.append(i)
        if((i!=0 and i!=n-1 and arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (i==n-1 and arr[i]>arr[i-1])):
            max_v.append(i)
    if(len(min_v)==len(max_v)):
        for i in range(0,len(min_v)):
            print("("+str(min_v[i])+" "+str(max_v[i])+")", end=" ")
            flag=1
    return flag


if __name__=="__main__":
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        arr=list(map(int,input().split()))
        #print(arr)
        flag=stock_buy_sell(arr)
        if(flag==0):
            print("No Profit")
        else:
            print("")
