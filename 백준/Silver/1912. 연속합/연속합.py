import sys
input=sys.stdin.readline

n=int(input())
arr=[0]+list(map(int,input().split()))

dp=[0]*(n+1)
dp[1]=arr[1]
for i in range(2,n+1):
    if dp[i-1]>0:
        dp[i]=dp[i-1]+arr[i]
    else:
        dp[i]=arr[i]
        
print(max(dp[1::]))