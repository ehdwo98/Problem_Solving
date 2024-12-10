import sys
input=sys.stdin.readline

n,l=map(int,input().split())
arr=sorted(list(map(int,input().split())))
ans=0
s=0
for a in arr:
    if s<a:
        s=a-0.5+l
        ans+=1
print(ans)