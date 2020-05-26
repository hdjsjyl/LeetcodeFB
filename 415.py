"""
415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# solution: time complexity: O(n)
# step1: reverse string
# computer one by one
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ''
        cnt = 0
        for i in range(min(len(num1), len(num2))):
            t1 = (int(num1[i]) + int(num2[i]) + cnt) % 10
            cnt = (int(num1[i]) + int(num2[i]) + cnt) // 10
            res += str(t1)
        if len(num2) > len(num1):
            for j in range(i + 1, len(num2)):
                t1 = (int(num2[j]) + cnt) % 10
                cnt = (int(num2[j]) + cnt) // 10
                res += str(t1)
        elif len(num1) > len(num2):
            for j in range(i + 1, len(num1)):
                t1 = (int(num1[j]) + cnt) % 10
                cnt = (int(num1[j]) + cnt) // 10
                res += str(t1)

        if cnt != 0:
            res += str(cnt)
        return res[::-1]