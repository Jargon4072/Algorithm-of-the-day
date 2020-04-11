
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