#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        if not list1 and not list2: return None

        out = ListNode()
        curr = out

        while list1 and list2:
            if list1.val < list2.val:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next
            curr.next = ListNode()
            curr = curr.next
                
        if list1:
            curr.val = list1.val
            curr.next = list1.next
        elif list2:
            curr.val = list2.val
            curr.next = list2.next
        
        return out
            
# @lc code=end

