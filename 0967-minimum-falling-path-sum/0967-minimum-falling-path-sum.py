class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1,len(A)):
            for j in range(1,len(A[0])-1):
                A[i][j] = A[i][j] + min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])
            
            A[i][0] = A[i][0] + min(A[i-1][0], A[i-1][1])
            A[i][-1] = A[i][-1] + min(A[i-1][-2], A[i-1][-1])
            
        return min(A[-1])