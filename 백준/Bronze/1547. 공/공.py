import sys
input=sys.stdin.readline

m=int(input())
res=1
for _ in range(m):
    x,y=map(int,input().split())
    if x==res:
        res=y
    elif y==res:
        res=x
print(res)