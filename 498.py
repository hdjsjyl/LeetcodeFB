"""
498. Diagonal Traverse
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

"""

## TC: O(mn)


from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = defaultdict(list)
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        for i in range(m):
            for j in range(n):
                res[i + j].append(matrix[i][j])
        re = []
        for i in range(m - 1 + n - 1 + 1):
            if i % 2 == 0:
                tmp = res[i]
                tmp.reverse()
                re += tmp
            else:
                re += res[i]

        return re