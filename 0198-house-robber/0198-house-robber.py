class Solution:
    def rob(self, arr: List[int]) -> int:
        n=len(arr)
        def f(ind,arr,dp):
            if dp[ind]!=-1:
                return dp[ind]
            if ind==0:
                return arr[ind]
            if ind<0:
                return 0
            pick = arr[ind] + f(ind-2, arr, dp)
            nonPick = 0 + f(ind-1, arr, dp)
            dp[ind] = max(pick, nonPick)
            return dp[ind]

        def solve(n, arr):
            dp = [-1 for i in range(n)]
            return f(n-1, arr, dp)
        return solve(n,arr)