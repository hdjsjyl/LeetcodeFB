"""
350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

# Solution: time complexity: O(n)
class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dict1 = {}
        dict2 = {}
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1

        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1

        dictr = {}
        for key, value in dict1.items():
            if key in dict2:
                dictr[key] = min(dict1[key], dict2[key])

        res = []
        for key, value in dictr.items():
            res += [key] * value

        return res