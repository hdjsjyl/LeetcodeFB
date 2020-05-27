"""
523. Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
"""

# solutions, presums % k
# if (n1 + n2) % k == 0, n1 % k == n2 % k
# finally, consider corner case, dicts[0] = -1

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presums = []
        for i in range(len(nums)):
            num = nums[i]
            if not presums:
                if k != 0:
                    presums.append([num % k, i])
                else:
                    presums.append([num, i])
            else:
                if k != 0:
                    presums.append([(presums[-1][0] + num) % k, i])
                else:
                    presums.append([(presums[-1][0] + num), i])

        dicts = {}
        dicts[0] = -1
        for cnt, idx in presums:
            if cnt not in dicts:
                dicts[cnt] = idx
            else:
                if idx - dicts[cnt] > 1:
                    return True

        return False

