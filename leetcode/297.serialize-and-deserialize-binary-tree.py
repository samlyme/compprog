#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree

from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        con = {}
        max_idx = 0
        
        def dfs(root: Optional[TreeNode], index: int):
            nonlocal max_idx
            if not root:
                return
            if index > max_idx:
                max_idx = index
            con[index] = root.val
            dfs(root.left, index * 2)
            dfs(root.right, index * 2 + 1)

        dfs(root, 1)
        out = []
        for i in range(1, max_idx + 1):
            out.append(con.get(i, 1001))
        return str(out)

        

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data[1:-1].split(", "))

        def dfs():
            val = next(vals)
            if val == "1001":
                return None
            node = TreeNode(int(val))
            node.left = dfs() # type: ignore
            node.right = dfs() # type: ignore
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

