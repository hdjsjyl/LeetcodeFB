"""
173. Binary Search Tree Iterator
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
"""

# solution1: inorder of binary search tree, time complexity: O(n); memory complexity: O(n);
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.stack.append(root.val)
        self.helper(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.stack:
            return self.stack.pop(0)
        return -1

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# solution2: recursive of binary search tree, time complexity: O(logn); memory complexity: O(h), h is the height of binary search tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root

    def helper(self, root, parent):
        if root.left:
            return self.helper(root.left, root)

        if root == parent:
            return root

        parent.left = root.right
        return root

    def next(self) -> int:
        """
        @return the next smallest number
        """

        tmp = self.helper(self.root, self.root)
        if tmp == self.root:
            res = self.root.val
            self.root = self.root.right
            return res
        else:
            return tmp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.root:
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()