# cook your dish here

for i in range(int(input())):
    n=int(input())
    a=2
    b=4
    d=1
    if n==0:
        print(-1)
    if n==1:
        print('1 4 3 2')
    if n==2:
        print('2 4 3 1')
    if n==3:
        print('3 8 2 1')
    if n==4:
        print('3 8 5 1')
    if n==5:
        print('3 8 4 1')
    if n>5:
        value=n
        value=value-1
        if value%2==0:
            c=value
        else:
            c=value+2
        print(a,b,c,d)