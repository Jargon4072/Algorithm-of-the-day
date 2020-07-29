def olr(l,r,arr):
    if arr[r-1]==1:
        ans="ODD"
    elif arr[r-1]==0:
        ans="EVEN"
    return ans
def flip(arr,x):
    if arr[x-1]==1:
        arr[x-1]=0
    elif arr[x-1]==0:
        arr[x-1]=1


if __name__=="__main__":
    n,q=map(int,input().split())
    arr=[int(x) for x in input().strip().split()]
    while q:
        query=[int(x) for x in input().strip().split()]
        if query[0]==1:
            fval=query[1]
            flip(arr,fval)
        elif query[0]==0:
            l=query[1]
            r=query[2]
            res=olr(l,r,arr)
            print(res)
        q=q-1

# NOTE: Lesson Learned! this question didn't needed any dfs concepts even though it was present in the category of DFS problems on hackerearth. So, before just going blindly after tags, we should think of appreach by using common sense. 