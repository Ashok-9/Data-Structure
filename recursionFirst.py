def f(c):
    if c==5:
        return 
    print(c)
    c+=1
    f(c)
c=0
f(c)