a,b,c=map(int,input().split())

def cal(a,b,c):
    if b==1:
        return a%c
    else:
        if b%2==0:
            return (cal(a,b//2,c)**2)%c
        else:
            return ((cal(a,(b-1)//2,c)**2)*cal(a,1,c))%c

res=cal(a,b,c)
print(res)