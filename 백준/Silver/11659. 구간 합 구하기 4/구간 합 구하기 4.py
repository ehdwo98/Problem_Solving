import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[0]+list(map(int,input().split()))

dp=[0]*100001
for k in range(1,n+1):
    dp[k]=dp[k-1]+arr[k]

for _ in range(m):
    i,j=map(int,input().split())
    ans=dp[j]-dp[i-1]
    print(ans)