import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(list(map(int,input().split())) for _ in range(n))
# print(arr)
m,k=map(int,input().split())
arr2=list(list(map(int,input().split())) for _ in range(m))
# print(arr2)

ans=[]
for a in range(n):
    tmp=[]
    for b in range(k):
        res=0
        for c in range(m):
            res+=arr[a][c]*arr2[c][b]
        tmp.append(res)
    ans.append(tmp)
for a in ans:
    print(*a)