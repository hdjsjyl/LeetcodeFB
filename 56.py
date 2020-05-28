"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

# solution1: time complexity: O(nlogn) + O(n), memory complexity: O(n)
# O(nlogn) is the time complexity of sorting algorithm
# O(n) is the time complexity of accessing to the element
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


# solution2: time complexity: O(nlogn) + O(n), memory complexity: O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) <= 1:
            return intervals

        idx = 0
        for i in range(1, len(intervals)):
            start1 = intervals[idx][0]
            end1 = intervals[idx][1]
            s = intervals[i][0]
            e = intervals[i][1]
            if s <= end1:
                start = min(start1, s)
                end = max(end1, e)
                intervals[idx] = [start, end]
            else:
                idx += 1
                intervals[idx] = [s, e]

        return intervals[:idx + 1]