# @Author: Dwivedi Chandan
# @Date:   2020-04-05T10:37:10+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-05-17T18:58:02+05:30

'''
Given an expression string exp , write a program to examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.

Example:

Input: exp = “[()]{}{[()()]()}”
Output: Balanced



Input: exp = “[(])”
Output: Not Balanced
'''

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if s=="":
            return True
        if len(s)==1:
            return False
        stack=deque()
        flag=0
        for i in range(len(s)):
            item=s[i]
            if item=="[" or item=="{" or item=="(":
                stack.append(item)
            elif item=="]" or item=="}" or item==")":
                if not stack:
                    return False
                val=stack.pop()
                flag=1
                if (item=="]" and val !="[") or (item=="}" and val !="{") or (item==")" and val !="("):
                    return False

        if flag==0 or stack:
            return False
        return True