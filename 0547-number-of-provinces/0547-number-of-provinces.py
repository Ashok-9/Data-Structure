class Solution:
    
    def findCircleNum(self, isConnected) -> int:
        n=len(isConnected)
        vis=set()
        c=0
        def dfs(i):
            for j in range(0,n):

                if isConnected[i][j]==1 and i!=j and j not in vis:
                    vis.add(j)
                    dfs(j)
        for i in range(0,n):
            
            if i not in vis:
                c+=1
                vis.add(i)
                dfs(i)
        return c