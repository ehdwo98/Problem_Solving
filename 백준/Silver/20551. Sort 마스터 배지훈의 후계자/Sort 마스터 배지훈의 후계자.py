import sys
input=sys.stdin.readline

n,m=map(int,input().split())

arr=sorted(list(int(input())for _ in range(n)))

idx=dict()
for i in range(n):
    if arr[i] not in idx:
        idx[arr[i]]=i

for i in range(m):
    res=int(input())
    if res in idx:
        print(idx[res])
    else:
        print(-1)