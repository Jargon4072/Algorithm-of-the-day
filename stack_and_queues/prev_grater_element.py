'''
Given an array of distinct elements, find previous greater element for every element. If previous greater element does not exist, print -1.

Examples:

Input : arr[] = {10, 4, 2, 20, 40, 12, 30}
Output :         -1, 10, 4, -1, -1, 40, 40

Input : arr[] = {10, 20, 30, 40}
Output :        -1, -1, -1, -1

Input : arr[] = {40, 30, 20, 10}
Output :        -1, 40, 30, 20
Expected time complexity : O(n)

'''

def prev_greater(arr):
    top=0
    res=[]
    for i in range(len(arr)):
        if i==0:
            res.append(-1)
            top=i
        else:
            if arr[i]>arr[top]:
                if res[top]==-1:
                    res.append(-1)
                    top=i
                elif res[top]>arr[i]:
                    res.append(res[top])
                    top=i
                else:
                    while arr[top]<=arr[i]:
                        top=top-1
                        if top==-1:
                            break
                    if top==-1:
                        res.append(-1)
                    else:
                        res.append(arr[top])
                    top=i
            else:
                res.append(arr[top])
                top=i
    return res


if __name__=="__main__":
    arr=[int(x) for x in input().strip().split()]
    print(prev_greater(arr))
