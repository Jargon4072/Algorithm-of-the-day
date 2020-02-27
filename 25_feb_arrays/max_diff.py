# @Author: Dwivedi Chandan
# @Date:   2020-02-26T07:39:31+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-02-27T20:58:08+05:30
#============================================= PROBLEM Statement ===============================================================
'''
You are given an array A (distinct elements) of size N. Find out the maximum difference between any two elements such that larger element appears after the smaller number in A.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line of each test case is N,N is the size of array. The second line of each test case contains N elements separated by spaces.

Output:
For each testcase, print the maximum difference between two element. Otherwise print -1

Constraints:
1 <= T <= 100
2 <= N <= 107
0 <= Ai <= 107

Example:
Input:
2
7
2 3 10 6 4 8 1
6
7 9 5 6 3 2

Output:
8
2
Explanation:
Testcase1:  Array is [2, 3, 10, 6, 4, 8, 1] then returned value is 8 (Diff between 10 and 2).
Testcase2: Array is [ 7, 9, 5, 6, 3, 2 ] then returned value is 2 (Diff between 7 and 9).
'''

#===================================================================================================================================






import collections

# approach: use deque and store smallest value at leftmost end and largest value at rightmost end.
def max_diff(arr):

    #initialise a dque and push arr[0] (i.e. first element)
    dq = collections.deque([arr[0]])
    diff=0
    flag=0
    for i in range(1,len(arr)):
        if(arr[i]>dq[-1]):
            # if the array element is grater than rightmost value of deque, push it on right.
            dq.append(arr[i])
            diff=max(diff,abs(dq[0]-arr[i]))        #maximum difference
            flag=1
        else:
            # if smaller values comes, pop until rightmost value becomes smaller or dq becomes empty.
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