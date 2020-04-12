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

