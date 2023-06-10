from collections import deque
class Solution:
    
    def findCircleNum(self, isConnected) -> int:
        n=len(isConnected)
        q=deque()
        vis=set()
        c=0
        def bfs(i):
            q.append(i)
            while q:
                i=q.popleft()
                for j in range(0,n):
                    if isConnected[i][j]==1 and i!=j and j not in vis:
                        q.append(j)
                        vis.add(j)
                    
        for i in range(0,n):
            
            if i not in vis:
                c+=1
                vis.add(i)
                bfs(i)
        return c