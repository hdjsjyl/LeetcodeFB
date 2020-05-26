"""
199. Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# solution1: DFS, time complexity: O(n), memory complexisty: O(n)
# to make sure we add the first element in each level to res,
# we have the depth parameter and check whether the length of res is equal to the depth or not.
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.helper(root, res, 0)
        return res

    def helper(self, root, res, depth):
        if not root:
            return

        if len(res) == depth:
            res.append(root.val)

        self.helper(root.right, res, depth + 1)
        self.helper(root.left, res, depth + 1)

# solution2: BFS, time complexity: O(n), memory complexity: O(n)
# traverse the elements for each level, which corresponds to the depth
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            res.append(stack[-1].val)
            for i in range(len(stack)):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        return res