'''
Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.
Examples :

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
Output: 3 3 4 5 5 5 6
Explanation:
Maximum of 1, 2, 3 is 3
Maximum of 2, 3, 1 is 3
Maximum of 3, 1, 4 is 4
Maximum of 1, 4, 5 is 5
Maximum of 4, 5, 2 is 5
Maximum of 5, 2, 3 is 5
Maximum of 2, 3, 6 is 6

Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4
Output: 10 10 10 15 15 90 90
Explanation:
Maximum of first 4 elements is 10, similarly for next 4
elements (i.e from index 1 to 4) is 10, So the sequence
generated is 10 10 10 15 15 90 90

'''


from collections import deque

def max_of_subarray(arr,k):
    n=len(arr)
    dq=deque()
    for i in range(k):
        while dq and arr[i]>arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    for i in range(k,n):
        print(arr[dq[0]],end=" ")

        while dq and dq[0]<=i-k:
            dq.popleft()
        while dq and arr[i]>=arr[dq[-1]]:
            dq.pop()
        dq.append(i)

    print(str(arr[dq[0]]))

if __name__=="__main__":
    print("Enter K: ")
    k=int(input())
    print("Enter array: ")
    arr=[int(x) for x in input().strip().split()]
    max_of_subarray(arr,k)

