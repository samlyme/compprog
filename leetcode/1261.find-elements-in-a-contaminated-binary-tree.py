#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        def gen(root: Optional[TreeNode], val: int):
            if not root:
                return
            root.val = val
            gen(root.left, val*2 + 1)
            gen(root.right, val*2 + 2)

        gen(root, 0)

    def find(self, target: int) -> bool:
        # Your FindElements object will be instantiated and called as such:
        # obj = FindElements(root)
        # param_1 = obj.find(target)
        def dfs(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if root.val == target:
                return True
            return dfs(root.left) or dfs(root.right)

        return dfs(self.root)
        # @lc code=end
