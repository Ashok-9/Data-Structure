def fib(n):
    if dp[n]==-1:
        dp[n]=fib(n-1)+fib(n-2)
    return dp[n]
n=int(input("enter the input:"))
dp=[-1]*(n)
dp[0]=0
dp[1]=1
print(fib(n-1))
print(dp)