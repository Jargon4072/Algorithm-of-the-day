# @Author: Dwivedi Chandan
# @Date:   2020-03-09T21:34:40+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-03-15T17:42:09+05:30
#----------------------------- Problem Statement --------------------------------------------------------------------------
'''
Given a linked list of N nodes. The task is to check if the the linked list has a loop. Linked list can contain self loop.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list and next line contains the data of linked list.

Output:
For each testcase, print "True", if linked list contains loop, else print "False".

User Task:
The task is to complete the function detectloop() which contains reference to the head as only argument. This function should return 1 if linked list contains loop, else return 0.

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= Data on Node <= 103

Example:
Input:
2
3
1 3 4
2
4
1 8 3 4
0

Output:
True
False

Explaination:
Testcase 1: In above test case N = 3. The linked list with nodes N = 3 is given. Then value of x=2 is given which means last node is connected with xth node of linked list. Therefore, there exists a loop.

Testcase 2: For N = 4
x = 0 means then lastNode->next = NULL, then the Linked list does not contains any loop.

Problem statement link: https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
'''
#------------------------------------------------------------------------------------------------------------------------


def detectLoop(head):    #problem asked to complete this function only
    tmp=head
    slow=head
    fast=head
    while (slow and fast and fast.next) is not None:
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
    return False