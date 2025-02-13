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
        if not head: return None
        if not head.next: return head

        out = head.next

        prev: ListNode = ListNode(next=head)
        l: ListNode = head
        r: ListNode = head.next
        
        while r and r.next:
            l.next = r.next
            r.next = l
            prev.next = r

            
            prev = l
            l = l.next
            if not l.next:
                return out
            r = l.next
            
        l.next = r.next
        r.next = l
        prev.next = r

        return out
        
# @lc code=end

