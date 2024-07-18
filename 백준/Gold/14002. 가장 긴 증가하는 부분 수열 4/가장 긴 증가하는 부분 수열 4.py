import sys
input=sys.stdin.readline

n=int(input())
arr=[0]+list(map(int,input().split()))

dp=[[0,[]] for _ in range(n+1)]
dp[1][0]=1
dp[1][1].append(arr[1])

for i in range(2,n+1):
    tmp=[]
    for j in range(i):
        if arr[i]>arr[j]:
            tmp.append(dp[j])
    a,b=sorted(tmp,key=lambda x:x[0])[-1]
    dp[i]=[a+1,b+[arr[i]]]

a,b=sorted(dp,key=lambda x:x[0])[-1]
print(a)
print(*b)