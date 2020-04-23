#===========================================PROBLEM Statement =====================================================================
'''
Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai 
where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The description of T test cases follows. Each test case contains an integer N denoting the size of the array, 
followed by N space separated numbers to be stored in array.

Output:
Output the total unit of water trapped in between the blocks.

User Task:
The task is to complete the function trappingWater() which returns the total amount of water that can be trapped.

Constraints:
1 <= T <= 100
3 <= N <= 107
0 <= Ai <= 108

Example:
Input:
2
4
7 4 0 9
3
6 9 9

Output:
10
0

Explanation:
Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water trapped is 10 units.

For better visualisation, please visit to original problem statement link: https://shorturl.at/jqyBF
'''
#===========================================================================================================================

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


