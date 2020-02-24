
def count_majority(arr):
    flag=0
    hash=[0*10000000]*10000000
    for i in arr:
        val=int(i)
        hash[val]+=1
        if(hash[val]>(n/2)):
            flag=1
            #print(hash[val])
            return int(i)
    if (flag==0):
        return -1

if __name__=="__main__":
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        arr=list(map(int,input().split()))
        #print(arr)
        val=count_majority(arr)
        print(val)
