import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    arr=sorted(list(list(map(int,input().split())) for _ in range(n)))
    # print(arr)
    ans=1
    best=0
    for i in range(1,n):
        if arr[i][1]<arr[best][1]:
            best=i
            ans+=1
    print(ans)