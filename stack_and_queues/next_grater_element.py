'''
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.

Examples:

For any array, rightmost element always has next greater element as -1.
For an array which is sorted in decreasing order, all elements have next greater element as -1.
a) For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.
Element       NGE
   4      -->   5
   5      -->   25
   2      -->   25
   25     -->   -1
b) For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows.

  Element        NGE
   13      -->    -1
   7       -->     12
   6       -->     12
   12      -->     -1

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
def next_grater(arr):
    new_arr=arr[::-1]     #it will reverse the array. (slicing technique)
    res=prev_greater(new_arr)
    res_final=res[::-1]   #reversing again the result
    return res_final


if __name__=="__main__":
    arr=[int(x) for x in input().strip().split()]
    print(next_grater(arr))