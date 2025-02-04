#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[0] * n for _ in range(n)]
       
        for init, term in connections:
            graph[init][term] = 1

        # is a tree with root zero
        # if you can reach a node from zero, then you must reorder the path
        count = 0
        frontier = deque([0])

        while frontier:
            curr = frontier.pop()
            
            for j in range(n):
                if curr == j: continue
                
                if graph[curr][j] == 1:
                    count += 1
                    frontier.append(j)
                    graph[curr][j] = 0
                elif graph[j][curr] == 1:
                    frontier.append(j)
                    graph[j][curr] = 0

        return count
        
        
# @lc code=end

