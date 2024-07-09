import sys
input=sys.stdin.readline

n=int(input())
arr=[[0,0]]
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp=[0]*(n+1)
for i in range(1,n+1):
    t,p=arr[i]
    if i+t-1>n:
        continue
    dp[i]+=p
    for j in range(i+t,n+1):
        dp[j]=max(dp[j],dp[i])

print(max(dp))