# @Author: Dwivedi Chandan
# @Date:   2020-04-07T02:35:45+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-05-17T19:07:22+05:30

'''
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

'''




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