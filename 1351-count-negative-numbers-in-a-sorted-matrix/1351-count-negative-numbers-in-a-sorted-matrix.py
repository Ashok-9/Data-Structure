class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    s+=1
        return s