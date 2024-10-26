import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

left,right=0,max(arr)

while left<=right:
    mid=(left+right)//2
    sum=0
    for a in arr:
        if a>mid:
            sum+=a-mid
    if sum>=m:
        ans=mid
        left=mid+1
    else:
        right=mid-1

print(ans)