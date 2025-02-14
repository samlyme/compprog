#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head
        
        dummy = ListNode(next=head)

        curr = dummy
        while curr and curr.next:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        
        return dummy.next
        
# @lc code=end

