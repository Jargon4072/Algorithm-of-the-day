#========================================================================================================================
'''
The cost of stock on each day is given in an array A[] of size N. 
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Input:
First line contains number of test cases T. 
First line of each test case contains an integer value N denoting the number of days, followed by an array of stock prices of N days.

Output:
For each testcase, output all the days with profit in a single line. 
And if there is no profit then print "No Profit".

Constraints:
1 <= T <= 100
2 <= N <= 103
0 <= Ai <= 104

Example
Input:
2
7
100 180 260 310 40 535 695
10
23 13 25 29 33 19 34 45 65 67

Output:
(0 3) (4 6)
(1 4) (5 9)

Explanation:
Testcase 1: We can buy stock on day 0, and sell it on 3rd day, which will give us maximum profit.

Note: Output format is as follows - (buy_day sell_day) (buy_day sell_day)
For each input, output should be in a single line.

'''
#================================================================================================================================
def stock_buy_sell(arr):
    flag=0
    if(len(arr)<=0):
        return
    min_v=[]
    max_v=[]
    n=len(arr)
    for i in range(0,len(arr)):
        if((i!=0 and i!=n-1 and arr[i]<arr[i-1] and arr[i]<arr[i+1]) or (i==0 and arr[i]<arr[i+1])):      #stores local mimima
            min_v.append(i)
        if((i!=0 and i!=n-1 and arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (i==n-1 and arr[i]>arr[i-1])):     #stores local maxima
            max_v.append(i)
    if(len(min_v)==len(max_v)):            #if equal no of local maxima and minima found, print each as pair
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
