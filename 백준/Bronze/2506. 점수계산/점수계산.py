import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
ans=0
res=1
for i in range(n):
    if arr[i]==1:
        ans+=res
        res+=1
    else:
        res=1
print(ans)