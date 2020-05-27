"""
Lintcode 386. Longest Substring with At Most K Distinct Characters
Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"
Challenge
O(n) time
"""

# solution: two pointers
from collections import defaultdict


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or k == 0:
            return 0
        res = 1
        left = 0
        right = 0
        cnt = 0
        dicts = {}
        while right < len(s):
            dicts[s[right]] = dicts.get(s[right], 0) + 1
            if dicts[s[right]] == 1:
                cnt += 1

            if cnt <= k:
                res = max(res, right - left + 1)
            else:
                while cnt > k:
                    dicts[s[left]] -= 1
                    if dicts[s[left]] == 0:
                        cnt -= 1
                    left += 1
            right += 1

        if cnt <= k:
            res = max(res, right - left)

        return res

