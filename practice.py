# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        if x%2==0:
            print('chefina')
        else:
            print('chef')
    elif abs(x-y)==1:
        if max(x,y)%2==0:
            print('chef')
        else:
            print('chefina')
    elif x>y:
        print('chef')
    else:
        print('chefina')
            
        