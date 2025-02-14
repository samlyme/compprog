#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        
        dummy = ListNode()
        curr = dummy
        
        while any(lists):
            min_idx = -1
            min_val = None
            for i, node in enumerate(lists):
                if not node: continue
                if min_val == None or node.val < min_val:
                    min_val = node.val
                    min_idx = i
                    
            curr.next = lists[min_idx]
            curr = curr.next
            lists[min_idx] = lists[min_idx].next
        
        return dummy.next
        
# @lc code=end

