"""
282. Expression Add Operators
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
"""

# solution: DFS， time complexity: O(n*4**N)
# for each expression, if we want to get value of this expression, we need O(n);
# for each position, it has four choices, '+', '-', '*' or None

# idea1: if we need to consider all combination of all numbers with more than 1 number
# the dfs needs to have a parameter with idx
# idea2: for multiplication, whatever, the previous operator is '+' or is '-',
# we can make it to one condition

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 1:
            if int(nums) == target:
                return [num]
            else:
                return []
        res = []
        self.helper(num, 0, target, -1, '', res, 0)
        return res

    def helper(self, nums, idx, target, last, path, res, sums):
        if idx == len(nums):
            if sums == target:
                res.append(path)
            return

        for i in range(idx, len(nums)):
            x = int(nums[idx:i + 1])
            if i > idx and nums[idx] == '0':
                continue
            if idx == 0:
                self.helper(nums, i + 1, target, x, nums[idx:i + 1], res, x)
            else:
                self.helper(nums, i + 1, target, x, path + '+' + nums[idx:i + 1], res, sums + x)
                self.helper(nums, i + 1, target, -x, path + '-' + nums[idx:i + 1], res, sums - x)
                self.helper(nums, i + 1, target, last * x, path + '*' + nums[idx:i + 1], res, sums - last + last * x)