import sys
input=sys.stdin.readline

T,W=map(int,input().split())

dp=[[0]*(W+1) for _ in range(T+1)]
arr=[0]+[int(input()) for _ in range(1,T+1)]

dp[1][0]=arr[1]%2
dp[1][1]=arr[1]//2
for i in range(2,T+1):
    for j in range(W+1):
        if j%2==0:
            res=arr[i]%2
        else:
            res=arr[i]//2
        dp[i][j]=max(dp[i-1][0:j+1])+res

print(max(dp[T]))