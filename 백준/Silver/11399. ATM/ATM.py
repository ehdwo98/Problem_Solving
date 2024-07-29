import sys
input=sys.stdin.readline

n=int(input())

P=list(map(int,input().split()))

P.sort()

ans,s=0,0
for i in range(n):
    s+=P[i]
    ans+=s

print(ans)