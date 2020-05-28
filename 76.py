"""
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

# solution: two pointers, time complexity: O(n)
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        wlens = float('inf')
        wres = ""
        left = 0
        right = 0
        cnt = 0
        dicts = {}
        for tt in t:
            dicts[tt] = dicts.get(tt, 0) + 1
            cnt += 1

        while right < len(s):
            if s[right] in dicts:
                dicts[s[right]] -= 1
                if dicts[s[right]] >= 0:
                    cnt -= 1

            if cnt == 0:
                while left <= right and cnt == 0:
                    if right - left + 1 < wlens:
                        wlens = right - left + 1
                        wres = s[left:right + 1]
                    if s[left] in dicts:
                        dicts[s[left]] += 1
                        if dicts[s[left]] > 0:
                            cnt += 1
                    left += 1

            right += 1
        return wres