# @Author: Dwivedi Chandan
# @Date:   2020-02-26T07:39:31+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-02-27T13:20:17+05:30

import collections

def max_diff(arr):
    dq = collections.deque([arr[0]])
    diff=0
    flag=0
    for i in range(1,len(arr)):
        if(arr[i]>dq[-1]):
            dq.append(arr[i])
            diff=max(diff,abs(dq[0]-arr[i]))
            flag=1
        else:
            while(dq and (dq[-1]>arr[i])):
                dq.pop()
            dq.append(arr[i])
            diff=max(diff,abs(dq[0]-arr[i]))

    if (flag==0):
        return -1

    else:
        return diff

def main():
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        arr=list(map(int,input().split()))
        #print(arr)
        val=max_diff(arr)
        print(val)

if __name__=="__main__":
    main()