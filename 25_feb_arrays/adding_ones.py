# @Author: Dwivedi Chandan
# @Date:   2020-02-27T14:17:22+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-02-27T14:36:13+05:30



def adding_ones(arr,n):
    res=[n*0]*n
    for i in range(len(arr)):
        for i in range(arr[i]-1,len(res)):
            res[i]+=1
    return res

def main():
    t=int(input())
    while t>0:
        t-=1
        z=list(map(int,input().split()))
        n=z[0]
        k=z[1]
        arr=list(map(int,input().split()))
        #print(arr)
        val=adding_ones(arr,n)
        for i in val:
            print(i,end=" ")
        print("")

if __name__=="__main__":
    main()