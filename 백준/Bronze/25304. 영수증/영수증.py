import sys
input=sys.stdin.readline

x=int(input())
n=int(input())
arr=list(list(map(int,input().split())) for _ in range(n))

ans=0
for ar in arr:
    a,b=ar
    ans+=a*b
if ans==x:
    print('Yes')
else:
    print('No')