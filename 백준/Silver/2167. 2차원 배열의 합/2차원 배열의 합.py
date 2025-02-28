import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(list(map(int,input().split())) for _ in range(n))
k=int(input())
for _ in range(k):
    ans=0
    i,j,x,y=map(int,input().split())
    for a in range(i,x+1):
        for b in range(j,y+1):
            ans+=arr[a-1][b-1]
    print(ans)