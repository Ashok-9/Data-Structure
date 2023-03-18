n=int(input("enter any number:"))
def f(c):
    if c==n:
        return
    print(c+1)
    c+=1
    
    f(c)
c=0

f(c)