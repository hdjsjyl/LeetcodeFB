"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

## stack, TC: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        dics = {}
        stack = []
        for i in range(len(height)):
            if not stack:
                stack.append(i)
            else:
                while stack and height[i] >= height[stack[-1]]:
                    dics[stack[-1]] = [i, -1]
                    stack.pop(-1)
                stack.append(i)

        for i in range(len(stack) - 1):
            if stack[i] in dics:
                dics[stack[i]][1] = stack[i + 1]
            else:
                dics[stack[i]] = [-1, stack[i + 1]]

        res = 0
        i = 0
        while i < len(height):
            if i not in dics:
                i += 1
                continue
            else:
                if dics[i][0] != -1:
                    j = dics[i][0]
                else:
                    j = dics[i][1]
                for k in range(i + 1, j):
                    res += min(height[i], height[j]) - height[k]
                i = j

        return res


