"""
689. Maximum Sum of 3 Non-Overlapping Subarrays
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
"""


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # step1: get sums from i to i+k-1
        sums = []
        tmp = 0
        for i in range(k - 1):
            tmp += nums[i]

        cnt = 0
        for i in range(k - 1, len(nums)):
            tmp += nums[i]
            sums.append(tmp - cnt)
            cnt += nums[i - k + 1]

        # step2: get prefix sums from left and get prefix sums from right
        l = []
        r = []
        l.append(0)
        for i in range(1, len(nums) - k + 1):
            if sums[l[i - 1]] >= sums[i]:
                l.append(l[i - 1])
            else:
                l.append(i)

        r.append(len(nums) - k)
        for i in range(len(nums) - k - 1, -1, -1):
            if sums[i] >= sums[r[len(nums) - k - 1 - i]]:
                r.append(i)
            else:
                r.append(r[len(nums) - k - 1 - i])

        r.reverse()

        # step3: get x, y, z
        ans = 0
        x = -1
        y = -1
        z = -1
        for i in range(k, len(nums) - k + 1 - k):
            if sums[l[i - k]] + sums[i] + sums[r[i + k]] > ans:
                ans = sums[l[i - k]] + sums[i] + sums[r[i + k]]
                x = l[i - k]
                y = i
                z = r[i + k]
            elif sums[l[i - k]] + sums[i] + sums[r[i + k]] == ans:
                if x > l[i - k]:
                    x = l[i - k]
                    y = i
                    z = r[i + k]
        return [x, y, z]