#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int: # type: ignore
        max_sum = float('-inf')
        curr_level = 1
        x = 1

        frontier = deque([root]) # type: ignore


        while frontier:
            level_sum = 0
            for _ in range(len(frontier)):
                curr = frontier.popleft()
                level_sum += curr.val
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)

            if level_sum > max_sum:
                max_sum = level_sum
                x = curr_level

            curr_level += 1
            
        return x

# @lc code=end

