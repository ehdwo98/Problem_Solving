n,p,q,x,y=map(int,input().split())

dic=dict()
dic[0]=1

def dp(n):
    if n<=0:
        return 1
    elif n in dic:
        return dic[n]
    dic[n]=dp(abs(n//p)-x)+dp(abs(n//q)-y)
    return dic[n]

print(dp(n))