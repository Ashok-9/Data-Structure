def f(ind,l,a):
    if ind==n:
        print(l)
        return
    l.append(a[ind])
    f(ind+1,l,a)
    l.pop()
    f(ind+1,l,a)
a=[3,1,2]
n=len(a)
l=[]
f(0,l,a)

#time complexity 2**n
#space complexity n