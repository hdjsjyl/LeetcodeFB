"""
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

# solution: two pointers -> sliding window, time complexity: O(n)
from copy import deepcopy


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dicts = {}
        cnt = 0
        for ss in p:
            dicts[ss] = dicts.get(ss, 0) + 1
            cnt += 1
        left = 0
        right = 0
        res = []
        while left < len(s) and right < len(s):
            if s[right] in dicts:
                dicts[s[right]] -= 1
                if dicts[s[right]] >= 0:
                    cnt -= 1

            if right >= len(p):
                if s[left] in dicts:
                    dicts[s[left]] += 1
                    if dicts[s[left]] > 0:
                        cnt += 1
                left += 1
            right += 1
            if cnt == 0:
                res.append(left)
        return res