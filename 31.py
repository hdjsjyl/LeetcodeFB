"""
31. Next Permutation
mplement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
"""

# solution:
# step1: find one element with index i, which makes array[i] < array[i+1].
# It is also that we find two elements in decreasing order from checking the last element to the first element
# step2: find the last element that is larger than array[i], for example element with index of j
# step3: swtch array i and array j
# step4: reverse all elements fron index with i+1 to the last element

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:
            nums.reverse()
            return

        idx2 = -1
        for j in range(idx + 1, len(nums)):
            if nums[j] > nums[idx]:
                idx2 = j

        self.switch(nums, idx, idx2)
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            self.switch(nums, left, right)
            left += 1
            right -= 1
        return

    def switch(self, nums, idx, idx2):
        tmp = nums[idx]
        nums[idx] = nums[idx2]
        nums[idx2] = tmp