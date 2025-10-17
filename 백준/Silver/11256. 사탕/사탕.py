import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    j,n=map(int,input().split())
    arr=sorted(list(list(map(int,input().split())) for _ in range(n)),key=lambda x: -(x[0]*x[1]))
    # print(arr)
    ans=0
    for a in arr:
        j-=(a[0]*a[1])
        ans+=1
        if j<=0:
            print(ans)
            break