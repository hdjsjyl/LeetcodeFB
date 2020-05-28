"""
140. Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
"""

# solution: DP + DFS
# DP is used to check whether the word could be seperated in terms of the words in the word array;
# An auxilary array is used to remember the indexes to seperate current words interval
# Finally, DFS is used to get all solutions
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dps = [False for i in range(len(s) + 1)]
        dps[0] = True
        idxes = [[] for i in range(len(s) + 1)]
        for i in range(len(s) + 1):
            for j in range(i):
                if dps[j] and s[j:i] in wordDict:
                    dps[i] = True
                    idxes[i].append(j)

        if not dps[-1]:
            return []
        res = []
        self.helper(idxes, s, len(s), [], res)
        return res

    def helper(self, idxes, s, idx, path, res):
        if idx == 0:
            tmp = path[::-1]
            res.append(' '.join(tmp))
            return

        for i in idxes[idx]:
            path.append(s[i:idx])
            self.helper(idxes, s, i, path, res)
            path.pop(-1)




