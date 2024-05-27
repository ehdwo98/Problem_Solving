import sys

input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    x,y=map(int,input().split())
    arr.append([x,y])

ans=[]
for i in range(n):
    cnt=1
    for j in range(n):
        x,y=arr[i]
        a,b=arr[j]
        if x<a and y<b:
            cnt+=1
    ans.append(cnt)

print(*ans)