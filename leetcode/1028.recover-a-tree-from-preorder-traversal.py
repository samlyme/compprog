#
# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
#
import re
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        vals = list(filter(None, traversal.split("-")))
        depths = list(filter(None, re.split(r"[0-9]", traversal)))

        root = TreeNode(int(vals[0]))
        stack.append(root)

        for i in range(len(depths)):
            depth = len(depths[i])

            curr = TreeNode(int(vals[i+1]))

            for _ in range(len(stack) - depth):
                stack.pop()

            parent = stack[-1]  # top of stack
            if not parent.left:
                parent.left = curr
            else:
                parent.right = curr
            stack.append(curr)

        return root


# @lc code=end
