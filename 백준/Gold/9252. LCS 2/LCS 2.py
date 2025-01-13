import sys
input=sys.stdin.readline

arr1=' '+input().rstrip()
arr2=' '+input().rstrip()

dp=list([""]*len(arr2) for _ in range(len(arr1)))

for i in range(1,len(arr1)):
    for j in range(1,len(arr2)):
        if arr1[i]==arr2[j]:
            dp[i][j]=dp[i-1][j-1]+arr1[i]
        else:
            if len(dp[i-1][j]) < len(dp[i][j-1]):
                dp[i][j]=dp[i][j-1]
            else:
                dp[i][j]=dp[i-1][j]

print(len(dp[-1][-1]))
if len(dp[-1][-1])!=0:
    print(''.join(dp[-1][-1]))