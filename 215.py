"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
"""

# Solution: Average time complexity: O(n), Worst time complexity: O(n**2)
# each time, we select a pivot value and check what is the position of this pivot value
# the time complexity is equal to: O(n) + O(n/2) + O(n/4) + O(n/8) + ... = O(n)
# if the position of this pivot value is equal to k-1, return
# elif the position of this pivot value is greater than k-1, recheck the left part;
# elif the position of this pivot value is smaller than k-1, recheck the right part;

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            idx = self.helper(nums, left, right)
            if idx == k - 1:
                return nums[idx]
            elif idx < k - 1:
                left = idx + 1
            else:
                right = idx - 1
        return nums[k - 1]

    def helper(self, nums, left, right):
        if left == right:
            return left
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] <= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] >= pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        return left
