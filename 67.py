"""
67. Add Binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""

# Solution: time complexity: O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        res = ''
        cnt = 0
        for i in range(min(len(a), len(b))):
            if a[i] == b[i] and a[i] == '1':
                res += str(cnt)
                cnt = 1
            elif int(a[i]) + int(b[i]) == 1 and cnt == 1:
                res += '0'
                cnt = 1
            else:
                res += str(int(a[i]) + int(b[i]) + cnt)
                cnt = 0

        if len(a) > len(b):
            for j in range(len(b), len(a)):
                if a[j] == '1' and cnt == 1:
                    res += '0'
                    cnt = 1
                else:
                    res += str(int(a[j]) + cnt)
                    cnt = 0
        elif len(b) > len(a):
            for j in range(len(a), len(b)):
                if b[j] == '1' and cnt == 1:
                    res += '0'
                    cnt = 1
                else:
                    res += str(int(b[j]) + cnt)
                    cnt = 0

        if cnt == 1:
            res += '1'

        return res[::-1]