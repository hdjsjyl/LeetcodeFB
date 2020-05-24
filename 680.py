"""
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
"""

# solution: time complexity: O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.helper(s, left + 1, right) or self.helper(s, left, right - 1)

        return True

    def helper(self, s, left, right):
        if left >= len(s) or right < 0 or left >= right:
            return True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True