"""
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# solution: the key point of binary tree is about the return value
# normally, the return value is directly related to the answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 1

    def helper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = self.helper(root.left)
        right = self.helper(root.right)
        self.res = max(self.res, left + right + 1)
        return max(left + 1, right + 1)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.helper(root)
        return self.res - 1