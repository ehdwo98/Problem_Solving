import sys
input=sys.stdin.readline

n=int(input())
A=[0]+list(map(int,input().split()))

dp=[0]*(n+1)
dp[1]=1

for i in range(2,n+1):
    c=1
    arr=[]
    for j in range(i-1,0,-1):
        if A[i]>A[j]:
            tmp=dp[j]+1
            arr.append(tmp)
            c=0
    if c:
        dp[i]=1
    else:
        dp[i]=max(arr)

print(max(dp[1::]))