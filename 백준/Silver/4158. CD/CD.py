import sys
input=sys.stdin.readline

while 1:
    n,m=map(int,input().split())
    if (n,m)==(0,0):
        break
    dic=dict()
    for _ in range(n):
        res=int(input())
        dic[res]=1

    ans=0
    for _ in range(m):
        res=int(input())
        if res in dic:
            ans+=1
    print(ans)