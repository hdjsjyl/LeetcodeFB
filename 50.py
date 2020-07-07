"""
50. Pow(x, n)
Medium

1484

2988

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
"""

# binary search , TC: log(n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x

        res = 1
        while n > 0:
            if n & 1:
                res *= x
            n = n >> 1
            x *= x

        return res