class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=False
        col=False
        m=len(matrix)
        n=len(matrix[0])
        for i in range(n):
            if matrix[0][i]==0:
                col=True
        for i in range(m):
            if matrix[i][0]==0:
                row=True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if row==True:
            for i in range(m):
                matrix[i][0]=0
        if col==True:
            for i in range(n):
                matrix[0][i]=0
        return matrix
        
s=Solution()
l=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(s.setZeroes(l))
        