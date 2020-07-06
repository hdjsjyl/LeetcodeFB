"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
"""

## binary search, TC: O(logn)
## bit operation: << means *2, >> means /2

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        flag = 1
        if dividend < 0:
            flag *= -1
            dividend *= -1
        if divisor < 0:
            flag *= -1
            divisor *= -1

        ant = 0
        while dividend >= divisor:
            cnt = 1
            while dividend >= divisor << cnt:
                cnt += 1
            ant += 1 << cnt - 1
            dividend -= divisor << cnt - 1

        res = ant * flag
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -1 * 2 ** 31:
            return -1 * 2 ** 31
        return ant * flag

