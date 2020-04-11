# @Author: Dwivedi Chandan
# @Date:   2020-04-07T02:35:45+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-04-12T01:28:04+05:30


def stock_span(arr):
    top=0
    s=[]
    for i in range(len(arr)):

        if arr[top]>arr[i] or i==0:
            top=i
            s.append(1)

        elif arr[top]<=arr[i]:
            count=0
            while arr[top]<=arr[i]:
                count=count+1
                top=top-1
                if top==-1:
                    break
            top=top+count+1
            s.append((count+1))

    return s

if __name__=="__main__":
    arr=[int(x) for x in input().strip().split()]
    print(stock_span(arr))