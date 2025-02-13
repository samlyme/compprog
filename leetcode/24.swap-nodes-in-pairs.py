#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy: ListNode = ListNode(next=head)
        l = dummy
        r = head
        
        while r and r.next:
            l.next = r.next
            r.next = l.next.next
            l.next.next = r
            
            l = r
            r = l.next

        return dummy.next
        
# @lc code=end

