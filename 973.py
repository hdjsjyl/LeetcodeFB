
# Solution1: time complexity: O(nLogK)
# n is the length of points list; K is length of stack we maintained
# because the question requires us to get first K points closest to original coordinate
# for this method, we maintain a stack with length of K,
#  each time, binary search is used to get the index of current point
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dislist = []
        for p in points:
            dis = p[0] ** 2 + p[1] ** 2
            if not dislist or dis >= dislist[-1][-1]:
                dislist.append([p, dis])
            elif dis <= dislist[0][-1]:
                dislist.insert(0, [p, dis])
            else:
                idx = self.helper(dislist, [p, dis])
                dislist.insert(idx, [p, dis])
            if len(dislist) > K:
                dislist.pop(-1)

        res = []
        for dis in dislist:
            res.append(dis[0])
        return res

    def helper(self, dis, p):
        left = 0
        right = len(dis) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if dis[mid][-1] == p[-1]:
                return mid
            elif dis[mid][-1] > p[-1]:
                right = mid
            else:
                left = mid

        if p[-1] < dis[left][-1]:
            return left
        elif p[-1] < dis[right][-1]:
            return right
        return right + 1

# Solution2: time complexity is O(nlogK)
# n is the length of points list
# using heap to maintain a heap with length of K
# each upate of heap cost logK time
# each time, pop the point with the largest distance to the original coordinate

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dislist = []
        heapq.heapify(dislist)
        for p in points:
            dis = p[0] ** 2 + p[1] ** 2
            heapq.heappush(dislist, [-dis, p])
            if len(dislist) > K:
                heapq.heappop(dislist)

        res = []
        while dislist:
            tmp = heapq.heappop(dislist)
            res.append(tmp[1])

        return res