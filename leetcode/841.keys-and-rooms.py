#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool: # type: ignore
        explored = set()
        frontier = deque([0])
        
        while frontier:
            curr = frontier.popleft() # doesnt matter if is dfs or bfs
            if curr not in explored:
                explored.add(curr)
                frontier.extend(rooms[curr])

        return len(explored) == len(rooms)
            
        
# @lc code=end

