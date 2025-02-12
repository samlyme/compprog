#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        if not head.next: return None

        dummy = ListNode(next=head)
        l = dummy
        r = dummy

        for _ in range(n):
            r = r.next

        while r.next:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        
        return dummy.next
# @lc code=end

