class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row=0
       
        n=len(mat)
        sum=0   
        while(row<=n-1):
            sum+=mat[row][row]
            row+=1
           
        row=0
        col=n-1
        while(row<=n-1):
            sum+=mat[row][col]
            row+=1
            col-=1
        if n%2==0:
            return sum
        else:
            odd=n//2
            sum=sum-mat[odd][odd]
            return sum  