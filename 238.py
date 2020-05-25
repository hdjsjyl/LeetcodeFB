"""
238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""
# solution: time complexity: O(n), memory complexity: O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 1
        r = 1
        res = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            res[i] *= l
            res[len(nums)-1-i] *= r
            l *= nums[i]
            r *= nums[len(nums)-1-i]
        return res