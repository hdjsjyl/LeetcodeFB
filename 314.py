"""
Lintcode: 651. Binary Tree Vertical Order Traversal
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example
Example1

Inpurt:  {3,9,20,#,#,15,7}
Output: [[9],[3,15],[20],[7]]
Explanation:
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
"""

# DFS
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import defaultdict


class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """

    def __init__(self):
        self.mins = float('inf')
        self.maxs = float('-inf')

    def verticalOrder(self, root):
        # write your code here
        if not root:
            return []

        dicts = defaultdict(list)

        self.helper(root, 0, 0, dicts)

        res = []
        for i in range(self.mins, self.maxs + 1):
            res.append([v[0] for v in sorted(dicts[i], key=lambda x: x[1])])
        return res

    def helper(self, root, x, y, dicts):
        if not root:
            return
        self.mins = min(self.mins, x)
        self.maxs = max(self.maxs, x)
        dicts[x].append([root.val, y])
        self.helper(root.left, x - 1, y + 1, dicts)
        self.helper(root.right, x + 1, y + 1, dicts)
