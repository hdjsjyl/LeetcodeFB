"""
Lintcode: 1534. Convert Binary Search Tree to Sorted Doubly Linked List
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:
"""

## solution inorder traverse of the tree
## idea1: cope with the head and tail element
## idea2: take care of the pre element and upate the left and right pointers

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def __init__(self):
        self.pre = None
        self.head = None
        self.last = None

    def treeToDoublyList(self, root):
        # Write your code here.
        ## 1. inorder
        ## 2. pre, head, last, cur

        if not root:
            return

        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root

        self.helper(root)
        self.head.left = self.last
        self.last.right = self.head
        return self.head

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)

        if not self.head:
            self.head = root

        if self.pre:
            self.pre.right = root
            root.left = self.pre
        self.pre = root

        self.last = root
        self.helper(root.right)