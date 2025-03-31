import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(x for x in range(n+1))
for _ in range(m):
    i,j=map(int,input().split())
    tmp=arr[i]
    arr[i]=arr[j]
    arr[j]=tmp
for a in arr[1:]:
    print(a,end=' ')