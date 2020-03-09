# @Author: Dwivedi Chandan
# @Date:   2020-03-09T21:34:40+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-03-09T23:48:24+05:30



def detectLoop(head):
    tmp=head
    slow=head
    fast=head
    while (slow and fast and fast.next) is not None:
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return True
    return False