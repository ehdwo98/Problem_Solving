k,n=map(int,input().split())
arr=[]
for _ in range(k):
    i=int(input())
    arr.append(i)
# print(arr)
s=1
e=max(arr)
while s<=e:
    mid=(s+e)//2
    sum=0
    for a in arr:
        sum+=a//mid
    if sum>=n:
        s=mid+1
    else:
        e=mid-1

print(s-1)