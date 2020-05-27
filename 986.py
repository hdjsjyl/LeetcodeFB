""""
986. Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)



Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""

# solution: two pointers, O(n)
# idea: to consider the cross condition totally
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            print(A[i], B[j])
            start1 = A[i][0]
            end1 = A[i][1]

            start2 = B[j][0]
            end2 = B[j][1]

            if start2 <= end1 and start1 <= end2:
                start = max(start1, start2)
                end = min(end1, end2)
                res.append([start, end])
            if end1 > end2:
                j += 1
            else:
                i += 1

        return res