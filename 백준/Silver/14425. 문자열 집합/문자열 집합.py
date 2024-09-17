import sys
input=sys.stdin.readline

n,m=map(int,input().split())

s=dict()
for i in range(n):
   s[input().rstrip()]=i

ans=0
for _ in range(m):
   tmp=input().rstrip()
   if tmp in s:
      ans+=1

print(ans)