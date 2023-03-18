class Solution:
    def maxProfit(self, prices) -> int:
        m=0
        mini=prices[0]
        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            m=max(prices[i]-mini,m)
        return m
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
