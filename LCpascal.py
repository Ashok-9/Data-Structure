class Solution:
    def generate(self, numRows: int) :
        n=numRows
        l1=[]
        for i in range(n):
            l=[]
            for j in range(i+1):
                if j==0 or j==i:
                    l.append(1)
                else:
                    sum=l1[i-1][j-1]+l1[i-1][j]
                    l.append(sum)
            l1.append(l)
        print(l1)
s=Solution()
s.generate(5)