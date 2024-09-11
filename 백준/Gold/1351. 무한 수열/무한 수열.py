import sys
input=sys.stdin.readline

n,p,q=map(int,input().split())

def dp(n):
   if n in dic:
      return dic[n]
   dic[n]=dp(n//p)+dp(n//q)
   return dic[n]

dic=dict()
dic[0]=1

print(dp(n))