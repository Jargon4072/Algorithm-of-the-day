# @Author: Dwivedi Chandan
# @Date:   2020-02-27T14:38:33+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-02-27T20:36:32+05:30



#=====================================================PROBLEM Statement=================================================================
'''
Given an array of N size. The task is to rotate array by d elements where d is less than or equal to N.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of three lines. The first line of each test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements. The third line of each test case contains "d" .

Output:
Corresponding to each test case, in a new line, print the modified array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 200
1 ≤ A[i] ≤ 1000

Example:
Input
1
5
1 2 3 4 5
2

Output
3 4 5 1 2
'''
#==============================================================================================================================


def rotate(arr,k):
    res=arr[k:]
    for i in range(0,k):
        res.append(arr[i])
    return res

def main():
    t=int(input())
    while t>0:
        t-=1
        n=int(input())
        arr=list(map(int,input().split()))
        #print(arr)
        k=int(input())
        val=rotate(arr,k)
        for i in val:
            print(i,end=" ")
        print("")

if __name__=="__main__":
    main()