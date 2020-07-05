"""
658. Find K Closest Elements
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.



Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""

## two pointers, TC: O(n)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        while len(arr) > k:
            if x - arr[0] > arr[-1] - x:
                arr.pop(0)
            else:
                arr.pop(-1)

        return arr  


## binary search , TC: O(logn)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #         while len(arr) > k:
        #             if x-arr[0] > arr[-1]-x:
        #                 arr.pop(0)
        #             else:
        #                 arr.pop(-1)

        #         return arr
        left = 0
        right = len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]