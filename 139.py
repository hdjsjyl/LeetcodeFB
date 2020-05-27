"""
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""

# solution: dynamic programming
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dps = [False for i in range(len(s) + 1)]
        dps[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dps[j] and s[j:i] in wordDict:
                    dps[i] = True
                    break

        return dps[-1]