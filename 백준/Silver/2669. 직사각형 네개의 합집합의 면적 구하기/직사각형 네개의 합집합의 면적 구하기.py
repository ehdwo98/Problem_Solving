import sys
input=sys.stdin.readline

arr=list([0]*101 for _ in range(101))

for _ in range(4):
    lx,ly,rx,ry=map(int,input().split())
    for a in range(lx,rx):
        for b in range(ly,ry):
            arr[a][b]=1
ans=0
for a in arr:
    ans+=sum(a)
print(ans)