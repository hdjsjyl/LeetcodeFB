"""
Lintcode 654. Sparse Matrix Multiplication

Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example
Example1

Input:
[[1,0,0],[-1,0,3]]
[[7,0,0],[0,0,0],[0,0,1]]
Output:
[[7,0,0],[-7,0,3]]
Explanation:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

# solution: time complexity O(mnk)
# beacuse the matrix is sparse, it includes many zeros;
# so before we multiply the corresponding elements, we can check whether it is equal to zero or not
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        # write your code here
        m = len(A)
        n = len(A[0])
        k = len(B[0])
        res = [[0 for i in range(k)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for p in range(k):
                        res[i][p] += A[i][j] * B[j][p]

        return res

