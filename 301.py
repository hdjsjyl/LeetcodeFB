"""
301. Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
"""

## Solution: DFS, time complexity: O(2**N * N)
## N is the length of the string

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = 0
        right = 0
        for ss in s:
            if ss == '(':
                left += 1
            elif ss == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        res = []
        self.helper(s, left, right, res, 0)
        return res

    def helper(self, s, left, right, res, idx):
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            if self.valid(s):
                res.append(s)
            return
        for i in range(idx, len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            if s[i] == '(':
                self.helper(s[:i] + s[i + 1:], left - 1, right, res, i)
            elif s[i] == ')':
                self.helper(s[:i] + s[i + 1:], left, right - 1, res, i)

    def valid(self, s):
        left = 0
        right = 0
        for ss in s:
            if ss == '(':
                left += 1
            elif ss == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left == 0 and right == 0