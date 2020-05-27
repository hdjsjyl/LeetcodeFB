"""
349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

# solution: hashtable
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dicts1 = {}
        for num in nums1:
            dicts1[num] = dicts1.get(num, 0) + 1

        dicts2 = {}
        for num in nums2:
            dicts2[num] = dicts2.get(num, 0) + 1

        for key, value in dicts2.items():
            if key in dicts1:   
                res.append(key)

        return res