"""
528. Random Pick with Weight
Medium

764

2222

Add to List

Share
Given an array w of positive integers, where w[i] describes the weight of index i(0-indexed), write a function pickIndex which randomly picks an index in proportion to its weight.

For example, given an input list of values w = [2, 8], when we pick up a number out of it, the chance is that 8 times out of 10 we should pick the number 1 as the answer since it's the second element of the array (w[1] = 8).



Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
"""

# binary search, TC: O(logn)
import random


class Solution:
    def __init__(self, w: List[int]):
        self.stack = [w[0]]
        for i in range(1, len(w)):
            self.stack.append(self.stack[-1] + w[i])

    def pickIndex(self) -> int:
        s = random.randint(1, self.stack[-1])
        left = 0
        right = len(self.stack) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.stack[mid] == s:
                return mid
            elif self.stack[mid] < s:
                left = mid
            else:
                right = mid

        if self.stack[left] >= s:
            return left
        return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()