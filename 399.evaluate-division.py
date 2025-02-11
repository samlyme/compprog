#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    graph = defaultdict(dict)
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # there is a bug in leetcode, where feilds do not get cleared
        # between runs, so you must reinistantiate the graph
        self.graph = defaultdict(dict)
        for equation, value in zip(equations, values):
            self.graph[equation[0]][equation[1]] = value
            self.graph[equation[1]][equation[0]] = 1.0 / value

        print(self.graph)
        return [self.bfs(query) for query in queries]
            
    def bfs(self, query: List[str]) -> float: 
        if query[0] not in self.graph.keys() or query[1] not in self.graph.keys():
            return -1.0
        if query[0] == query[1]:
            return 1.0

        explored = set()
        frontier = deque([(query[0], 1)])
        
        while frontier:
            curr, cost = frontier.pop()
            for key in self.graph[curr].keys():
                if key == query[1]:
                    return cost * self.graph[curr][key]
                if key not in explored:
                    frontier.append((key, cost * self.graph[curr][key]))
            explored.add(curr)

        return -1.0
                
        
# @lc code=end

