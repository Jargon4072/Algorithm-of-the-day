#=========================================PROBLEM Statement ==============================================
'''
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. 
Also, the rightmost element is always a leader.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print all the leaders.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= Ai <= 107

Example:
Input:
3
6
16 17 4 3 5 2
5
1 2 3 4 0
5
7 4 5 7 3
Output:
17 5 2
4 0
7 7 3

Explanation:
Testcase 3: All elements on the right of 7 (at index 0) are smaller than or equal to 7.
 Also, all the elements of right side of 7 (at index 3) are smaller than 7. 
And, the last element 3 is itself a leader since no elements are on its right.
'''
#======================================================================================================================

def leaders(arr):
    res=[]
    max=arr[len(arr)-1]
    n=len(arr)-1
    for i in range(0,len(arr)):
        if(arr[n-i]>=max):           # traverse from right and compare each element with max
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
