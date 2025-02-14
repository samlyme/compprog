#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from heapq import heapify, heappop, heappush
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
        
        pq = [(x.val, idx, x) for idx, x in enumerate(lists) if x is not None]
        if len(pq) == 0: return None
        
        heapify(pq)

        # This is needed because python is a trash lang
        # essentially, when given an iterable as an item for a heap, it will
        # give the first value the most weight, then the next.
        # for us, if the val is tie, we dont care, so i keep a counter that 
        # essentially prioritizes the earlier elements.
        count = len(lists)
        dummy = ListNode()
        head = dummy
        while pq:
            curr = heappop(pq)[2]
            head.next = curr
            head = head.next
            
            if curr.next:
                heappush(pq, (curr.next.val, count, curr.next))
                count += 1

        return dummy.next
            
        
# @lc code=end

