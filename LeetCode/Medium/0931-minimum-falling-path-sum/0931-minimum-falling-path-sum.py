from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        INF = int(1e9)
        for i in range(1,n):
            for j in range(n):
                left = matrix[i-1][j-1] if j-1 >= 0 else INF 
                right = matrix[i-1][j+1] if j+1 < n else INF 
                matrix[i][j] += min(left,matrix[i-1][j],right)
        return min(matrix[n-1])