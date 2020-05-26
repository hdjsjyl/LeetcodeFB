"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""

# solution: BFS
# idea1: For serialize,   BFS traverses the binary tree and adds the None element
# idea2: For deserialize, another stack keeps the nodes without including None element
# idea3: For deserialize, slow and fast pointers; slow pointer is in the another stack for nodes without including None
# idea4: For deserialize, fast pointer is in the stack for nodes with including None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        res = []
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if not cur:
                res.append(cur)
                continue
            res.append(cur.val)

            stack.append(cur.left)
            stack.append(cur.right)

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        for i in range(len(data)):
            if data[i] is not None:
                data[i] = TreeNode(data[i])
        nodes = []
        nodes.append(data[0])
        slow = 0
        fast = 1
        while fast < len(data):
            nodes[slow].left = data[fast]
            nodes[slow].right = data[fast + 1]
            if nodes[slow].left:
                nodes.append(nodes[slow].left)
            if nodes[slow].right:
                nodes.append(nodes[slow].right)
            slow += 1
            fast += 2

        return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))