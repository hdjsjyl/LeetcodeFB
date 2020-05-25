"""
124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
"""

# Solution: recursive, time complexity: O(n)
# n is the number of nodes in the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = float('-inf')

    def helper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            self.res = max(self.res, root.val)
            return root.val
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.res = max(self.res, root.val + left + right, root.val, root.val + left, root.val + right)
        return max(root.val, root.val + left, root.val + right)

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.helper(root)
        return self.res