class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        i=len(grid)-1
        j=len(grid[0])-1
        dp=[[-1 for j in range(j+1)]for i in range(i+1)]
        def f(i,j):
          
            if i>=0 and j>=0 and grid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j)
            left=f(i,j-1)
            dp[i][j]=up+left
            return dp[i][j]
        return f(i,j)