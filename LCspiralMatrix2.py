class Solution:
    def generateMatrix(self, n: int) :
        top=0
        down=n-1
        left=0
        right=n-1
        l1=[]
        l=[]
        for _ in range(n):
            for _ in range(n):
                l1.append(0)
            l.append(l1)
            l1=[]
        temp=1
        dir=0
        while(left<=right and top<=down):
            if dir==0:
                for i in range(left,right+1):
                    l[top][i]=temp
                    temp+=1
                top+=1
            elif dir==1:
                for i in range(top,down+1):
                     l[i][right]=temp
                     temp+=1
                right-=1
            elif dir==2:
                for i in range(right,left-1,-1):
                     l[down][i]=temp
                     temp+=1
                down-=1
            elif dir==3:
                for i in range(down,top-1,-1):
                     l[i][left]=temp
                     temp+=1
                left+=1
            dir=(dir+1)%4
        return l
s=Solution()
#n=int(input())
print(s.generateMatrix(3))
  