from itertools import combinations

n,m=map(int,input().split())
arr=[i+1 for i in range(n)]

ans=list(combinations(arr,m))

for a in ans:
    print(*a)