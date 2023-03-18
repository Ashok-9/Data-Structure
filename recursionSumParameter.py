def f(c,sum,n):
    if c==n:
        print(sum)
        return
    f(c+1,sum+c,n)
f(1,0,5)
