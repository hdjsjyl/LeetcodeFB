"""
767. Reorganize String
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
"""

# solution: heap for frequency, time complexity: O(nlogn)
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        dicts = {}
        for ss in S:
            dicts[ss] = dicts.get(ss, 0) + 1

        resLists = []
        heapq.heapify(resLists)
        for key, value in dicts.items():
            heapq.heappush(resLists, [-value, key])

        res = ''
        while resLists:
            a1 = heapq.heappop(resLists)
            res += a1[1]
            if resLists:
                a2 = heapq.heappop(resLists)
                res += a2[1]
                if a2[0] + 1 < 0:
                    heapq.heappush(resLists, [a2[0] + 1, a2[1]])
            if a1[0] + 1 < 0:
                heapq.heappush(resLists, [a1[0] + 1, a1[1]])
        if res[-1] == res[-2]:
            return ''
        return res


