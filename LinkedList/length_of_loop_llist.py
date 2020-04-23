#---------------------------------- Problem Statement --------------------------------
'''
Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks whether a given Linked List contains loop or not and if loop is present then return the count of nodes in loop or else return 0.

Input :
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list and next line contains data of the linked list, and the third line contains the position of the node from beginning (0 based indexing) to which the last node will be connected to form a loop.
Note: If the input of the third line is zero then there is no loop.

Output:
For each testcase, there will be a single line of output containing the length of loop in linked list, else print 0, if loop is not present in the linked list.

User Task:
The task is to complete the function countNodesinLoop() which contains the only argument as reference to head of linked list.

Constraints:
1 <= T <= 100
1 <= N <= 500

Example:
Input:
2
10
25 14 19 33 10 21 39 90 58 45
4
2
1 0
1
Output:
6
1

Explanation:
Testcase 1: The loop is 45->10. So length of loop is 10->21->39->90->58->45 = 6. The number 10 is connected to the last node to form the loop because according to the input the 4th node from the beginning(0 based index) will be connected to the last node for the loop.
Testcase2:  The length of loop is 1.

Problem statement link: https://practice.geeksforgeeks.org/problems/find-length-of-loop/1
'''
#------------------------------------------------------------------------------------------------------------------------------

def countNodesinLoop(head): #had to write this function only.
    if head is None:
        return 0

    slow=head
    fast=head
    flag=0
    while (slow and slow.next and fast and fast.next and fast.next.next):
        if(slow==fast and flag!=0):
            count=1
            slow=slow.next
            while(slow!=fast):
                slow=slow.next
                count=count+1
            return count

        slow=slow.next
        fast=fast.next.next
        flag=1
    return 0


