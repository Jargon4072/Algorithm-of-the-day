#===============================Problem Statement =====================================================================
'''
Given an array A of N elements. Find the majority element in the array.
 A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Input:
The first line of the input contains T denoting the number of testcases. 
The first line of the test case will be the size of array and second line will be the elements of the array.

Output:
For each test case the output will be the majority element of the array.
 Output "-1" if no majority element is there in the array.

Constraints:
1 <= T<= 100
1 <= N <= 107
0 <= Ai <= 106

Example:
Input:
2
5
3 1 3 3 2
3
1 2 3

Output:
3
-1

Explanation:
Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.
'''
#=========================================================================================================================


def count_majority(arr):
    flag=0
    hash=[0*10000000]*10000000       #todo: optimise for memory
    for i in arr:
        val=int(i)
        hash[val]+=1             #concept of hashing is used. hash[] used to store count of each element
        if(hash[val]>(n/2)):
            flag=1
            #print(hash[val])
            return int(i)    #todo: for multiple majority
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
