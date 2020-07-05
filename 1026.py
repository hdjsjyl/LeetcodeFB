"""
1026. Maximum Difference Between Node and Ancestor
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)



Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""

## DFS, TC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.helper(root, root.val, root.val)
        return self.res

    def helper(self, node, mins, maxs):
        if not node:
            return
        self.res = max(abs(node.val - mins), abs(node.val - maxs), self.res)
        mins = min(mins, node.val)
        maxs = max(maxs, node.val)
        self.helper(node.left, mins, maxs)
        self.helper(node.right, mins, maxs)