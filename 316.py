"""
316. Remove Duplicate Letters
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
"""

# solution1: time complexity: O(n), memory complexity: O(n)
# using a auxiliary stack and build a increasing order stack
# using a set to judge whether the current element is in the stack or not
# using a dictionary to compute the frequency of each element

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        dicts = {}
        for ss in s:
            dicts[ss] = dicts.get(ss, 0) + 1

        stack = [s[0]]
        sets = set()
        sets.add(s[0])
        dicts[s[0]] -= 1

        for i in range(1, len(s)):
            dicts[s[i]] -= 1
            if s[i] in sets:
                continue
            else:
                while stack and ord(s[i]) < ord(stack[-1]) and dicts[stack[-1]] > 0:
                    sets.remove(stack.pop(-1))
                stack.append(s[i])
                sets.add(s[i])

        return ''.join(stack)