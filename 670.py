"""
670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
"""

# solution: time complexity is O(n); memory complexity is O(n);
# idea: sweeping the array from right to left
class Solution:
    def maximumSwap(self, num: int) -> int:
        strs = str(num)
        max_idx = len(strs) - 1
        max_dig = strs[-1]
        left = -1
        right = -1

        for i in range(len(strs) - 2, -1, -1):
            if strs[i] > max_dig:
                max_idx = i
                max_dig = strs[i]
                continue

            if strs[i] < max_dig:
                left = i
                right = max_idx

        if left == -1:
            return num
        lis = list(strs)
        tmp = lis[left]
        lis[left] = lis[right]
        lis[right] = tmp

        return int(''.join(lis))