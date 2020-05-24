## quick sort
## time complexity O(nlogn)

class Solution:
    def helper(self, nums, left, right):
        if left >= right:
            return
        start = left
        end = right
        pivot = nums[left + (right - left) // 2]
        while left <= right:
            while left <= right and nums[right] > pivot:
                right -= 1
            while left <= right and nums[left] < pivot:
                left += 1

            if left <= right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                right -= 1
                left += 1

        self.helper(nums, start, right)
        self.helper(nums, left, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        left = 0
        right = len(nums) - 1
        self.helper(nums, left, right)
        return nums