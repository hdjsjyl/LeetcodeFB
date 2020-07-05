"""
Lintcode: 663. Walls and Gates
中文English
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

Example
Example1

Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

# DFS, TC: O(n)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms):
        # write your code here
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        if n == 0:
            return

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.helper(rooms, i, j, 0)

    def helper(self, rooms, i, j, dis):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or rooms[i][j] < dis:
            return
        rooms[i][j] = dis
        dis += 1

        self.helper(rooms, i + 1, j, dis)
        self.helper(rooms, i, j + 1, dis)
        self.helper(rooms, i - 1, j, dis)
        self.helper(rooms, i, j - 1, dis)
