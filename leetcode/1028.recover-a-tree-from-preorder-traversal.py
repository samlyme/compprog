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
        latest = {}
        vals = list(filter(None, traversal.split("-")))
        depths = list(filter(None, re.split(r"[0-9]", traversal)))

        latest[0] = TreeNode(int(vals[0]))

        for i in range(len(depths)):
            depth = len(depths[i])

            latest[depth] = TreeNode(int(vals[i+1]))

            if not latest[depth-1].left:
                latest[depth-1].left = latest[depth]
            else:
                latest[depth-1].right = latest[depth]

        return latest[0]


# @lc code=end
