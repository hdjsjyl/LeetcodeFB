"""
Lintcdoe 900: Cloest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Example
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
"""

# solution: traverse of the binary search tree
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def __init__(self):
        self.res = None
        self.flag = False

    def closestValue(self, root, target):
        # write your code here
        if not root:
            return -1

        if target == root.val:
            return root.val
        self.res = root.val
        if target > root.val:
            self.helper(root.right, target)
        else:
            self.helper(root.left, target)
        return self.res

    def helper(self, root, target):
        if self.flag:
            return True
        if not root:
            return
        if target == root.val:
            self.flag = True
            self.res = root.val
            return
        if abs(target - root.val) < abs(self.res - target):
            self.res = root.val
        if target > root.val:
            self.helper(root.right, target)
        elif target < root.val:
            self.helper(root.left, target)