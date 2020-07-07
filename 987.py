"""
987. Vertical Order Traversal of a Binary Tree
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
"""

## DFS, TC: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def __init__(self):
        self.mins = float('inf')
        self.maxs = float('-inf')

    def helper(self, root, x, y, dicts):
        if not root:
            return
        dicts[y].append([x, root.val])
        self.mins = min(self.mins, y)
        self.maxs = max(self.maxs, y)
        self.helper(root.left, x + 1, y - 1, dicts)
        self.helper(root.right, x + 1, y + 1, dicts)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dicts = defaultdict(list)
        self.helper(root, 0, 0, dicts)
        res = []
        for i in range(self.mins, self.maxs + 1):
            res.append([v for k, v in sorted(dicts[i])])
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def __init__(self):
        self.mins = float('inf')
        self.maxs = float('-inf')

    def helper(self, root, x, y, dicts):
        if not root:
            return
        dicts[x].append([y, root.val])
        self.mins = min(self.mins, x)
        self.maxs = max(self.maxs, x)
        self.helper(root.left, x - 1, y - 1, dicts)
        self.helper(root.right, x + 1, y - 1, dicts)

    def cmp(self, v1, v2):
        if v1[0] != v2[0]:
            return v2[0] - v1[0]
        else:
            return v1[1] - v2[1]

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dicts = defaultdict(list)
        self.helper(root, 0, 0, dicts)
        res = []
        for i in range(self.mins, self.maxs + 1):
            res.append([v for k, v in sorted(dicts[i], key=cmp_to_key(self.cmp))])
        return res