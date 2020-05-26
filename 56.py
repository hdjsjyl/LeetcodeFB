"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

# solution: time complexity: O(nlogn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x:x[1])
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        res.append(intervals.pop(0))
        start = res[0][0]
        end = res[0][1]
        for i in range(len(intervals)):
            start1 = intervals[i][0]
            end1 = intervals[i][1]
            if start1 <= end:
                start = min(start1, start)
                end = max(end1, end)
                res.pop(-1)
                res.append([start, end])
            else:
                res.append([start1, end1])
                start = start1
                end = end1
        return res