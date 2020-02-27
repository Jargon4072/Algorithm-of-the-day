#================================================= Problem Statement ======================================
'''
Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case contains a single integer N denoting the size of array and the size of subarray K. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum for every subarray of size k.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ K ≤ N
0 ≤ A[i] <= 107

Example:
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90

Explanation:
Testcase 1: Starting from first subarray of size k = 3, we have 3 as maximum. Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6.

'''
#==========================================================================================================




import heapq as hpq

def max_subarr_sizek(arr,k):
    res=[]
    i = 0
    j = k-1
    h = arr[i:j + 1]
    hpq._heapify_max(h)
    #print(h[0], end =" ")
    res.append(h[0])                      #after heapify, top element will be maximum of all
    last = arr[i]
    i+= 1
    j+= 1
    next = arr[j]

    while j < n:

        h[h.index(last)] = next

        hpq._heapify_max(h)
        #print(h[0], end =" ")
        res.append(h[0])
        last = arr[i]
        i+= 1
        j+= 1
        if j < n:
            next = arr[j]

    return res

if __name__=="__main__":
    t=int(input())
    while t>0:
        t-=1
        x=list(map(int,input().split()))
        n=int(x[0])
        k=int(x[1])
        arr=list(map(int,input().split()))
        result=max_subarr_sizek(arr,k)
        for i in range(len(result)):
            print(result[i], end=" ")

        print("")