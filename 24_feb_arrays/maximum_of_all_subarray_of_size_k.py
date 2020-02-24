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