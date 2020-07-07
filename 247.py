"""
776. Strobogrammatic Number II
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

Example
Example 1:

Input: n = 2,
Output: ["11","69","88","96"]
Example 2:

Input: n = 1,
Output: ["0","1","8"]
"""

# DFS

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """

    def __init__(self):
        self.ones = ['0', '1', '8']
        self.twos = ['00', '11', '69', '96', '88']

    def findStrobogrammatic(self, n):
        # write your code here
        res = []
        self.helper(n, '', res)
        return res

    def helper(self, n, s, res):
        if n == 0:
            res.append(s)
            return

        if n % 2 == 1:
            for o in range(len(self.ones)):
                self.helper(n - 1, s + self.ones[o], res)
        else:
            if n == 2:
                for i in range(1, len(self.twos)):
                    self.helper(n - 2, self.twos[i][0] + s + self.twos[i][1], res)
            else:
                for i in range(len(self.twos)):
                    self.helper(n - 2, self.twos[i][0] + s + self.twos[i][1], res)