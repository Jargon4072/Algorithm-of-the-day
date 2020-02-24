import math

def trappingWater(a,n):
    res = 0
    left_max = 0
    right_max = 0
    left = 0
    right = n - 1
    while left <= right:            #iterate from left and right
        if a[left] <= a[right]:
            if left_max < a[left]:
                left_max = a[left]
            else:
                res += left_max - a[left]
            left += 1
        else:
            if right_max < a[right]:
                right_max = a[right]
            else:
                res += right_max - a[right]
            right -= 1
    return res






def main():
        T=int(input())
        while(T>0):

            n=int(input())

            arr=[int(x) for x in input().strip().split()]
            print(trappingWater(arr,n))


            T-=1


if __name__ == "__main__":
    main()


