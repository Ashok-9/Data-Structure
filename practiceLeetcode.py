
class Solution:
    def spiralOrder(self, matrix):
        top=0
        down=len(matrix)-1
        left=0

        right=len(matrix[0])-1
        l=[]
        dir=0
        while(left<=right and top<=down):
            if dir==0:
                for i in range(left,right+1):
                    l.append(matrix[top][i])
                top+=1
            elif dir==1:
                for i in range(top,down+1):
                    l.append(matrix[i][right])
                right-=1
            elif dir==2:
                for i in range(right,left-1,-1):
                    l.append(matrix[down][i])
                down-=1
            elif dir==3:
                for i in range(down,top-1,-1):
                    l.append(matrix[i][left])
                left+=1
            dir=(dir+1)%4
        return l
            
s=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))
            


            