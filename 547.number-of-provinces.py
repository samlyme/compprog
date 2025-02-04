#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
import collections
import enum

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int: # type: ignore
        explored = set()
        frontier = deque()  # type: ignore
        count = 0
        
        for city in range(len(M)):
            if city in explored: continue
            
            count += 1

            explored.add(city)
            
            for idx, connection in enumerate(M[city]):
                if connection == 1:
                    frontier.append(idx)

            while frontier:
                curr = frontier.pop()
                if curr in explored: continue
                
                explored.add(curr)
                
                for idx, connection in enumerate(M[curr]):
                    if connection == 1:
                        frontier.append(idx)
        
        return count
        
# @lc code=end

