"""
398. Random Pick Index
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""

# solution: build a list for each key, produce a random value in terms of the length of the list of each key
# time complexity: O(n)
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.dicts = defaultdict(list)
        for i in range(len(nums)):
            self.dicts[nums[i]].append(i)

    def pick(self, target: int) -> int:
        if len(self.dicts[target]) == 0:
            return self.dicts[target]
        length = len(self.dicts[target])
        idx = random.randint(0, length-1)
        return self.dicts[target][idx]